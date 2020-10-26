const child = require("child_process");
const fs = require("fs");

// const latestTag = child.execSync('git describe --long').toString('utf-8').split('-')[0];
// const output = child
//   .execSync(`git log ${latestTag}..HEAD --format=%B%H----DELIMITER----`)
//   .toString("utf-8");

const output = child
  .execSync(`git log --format=%B%H----DELIMITER----`)
  .toString("utf-8");

const commitsArray = output
  .split("----DELIMITER----\n")
  .map(commit => {
    const [message, sha] = commit.split("\n");

    return { sha, message };
  })
  .filter(commit => Boolean(commit.sha));

const currentChangelog = fs.readFileSync("./CHANGELOG.md", "utf-8");
const currentVersion = Number(require("./release_version.json").version);
const newVersion = new Date().toISOString().split("T")[0]

// 用version和时间作为release 标记
let newChangelog = `${
  new Date().toISOString().split("T")[0]
}\n\n`;

const features = [];
const Bugfixes = [];

// 分别维护features和bugfixes的内容，并将message和commit的链接进行绑定
commitsArray.forEach(commit => {
  if (commit.message.startsWith("newfeature: ")) {
    features.push(
      `* ${commit.message.replace("newfeature: ", "")} ([${commit.sha.substring(
        0,
        6
      )}](https://github.com/BaronStack/release_notes/commit/${
        commit.sha
      }))\n`
    );
  }
  if (commit.message.startsWith("bugfix: ")) {
    Bugfixes.push(
      `* ${commit.message.replace("bugfix: ", "")} ([${commit.sha.substring(
        0,
        6
      )}](https://github.com/BaronStack/release_notes/commit/${
        commit.sha
      }))\n`
    );
  }
});

if (features.length) {
  newChangelog += `## NewFeature\n`;
  features.forEach(feature => {
    newChangelog += feature;
  });
  newChangelog += '\n';
}

if (Bugfixes.length) {
  newChangelog += `## Bugfixes\n`;
  bugfixes.forEach(bugfix => {
    newChangelog += bugfix;
  });
  newChangelog += '\n';
}

// prepend the newChangelog to the current one
fs.writeFileSync("./CHANGELOG.md", `${newChangelog}${currentChangelog}`);
// update package.json
fs.writeFileSync("./release_version.json", JSON.stringify({ version: String(newVersion) }, null, 2));

// create a new commit
child.execSync('git add .');
child.execSync(`git commit -m "chore: Bump to version ${newVersion}"`);

// tag the commit
child.execSync(`git tag -a -m "Tag for version ${newVersion}" version${newVersion}`);