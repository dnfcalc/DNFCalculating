const currentVersion = (require("./Bulid/release_version.json").version).toString();
const child = require("child_process");
const gitVersion = child
.execSync(`git log --format=%B%H----DELIMITER----`)
.toString("utf-8");

if(currentVersion!=gitVersion){
  const newVersion = new Date().toISOString().split("T")[0]
  const fs = require("fs");
  
  const output = child
    .execSync(`git log --format=%B%H----DELIMITER----`)
    .toString("utf-8");
  
  const commitsArray = output
    .split("----DELIMITER----\n")
    .map(commit => {   
      let data = commit.split("\n");
      let returndata = ['',''];
      let i = 0
      for(i;i<data.length-1;i++){
         returndata[0]+=data[i]+(i<data.length-2?'<br>\n':'')
       }
      const [message, sha] = [returndata[0],data[data.length-1]];
      return {sha, message };
    })
    .filter(commit => Boolean(commit.sha));
  
  const currentChangelog = fs.readFileSync("./CHANGELOG.md", "utf-8");
  
  
  // 用version和时间作为release 标记
  let newChangelog = `# ${
    new Date().toISOString().split("T")[0]
  }\n\n`;
  
  const features = [];
  const Bugfixes = [];
  
  // 分别维护features和bugfixes的内容，并将message和commit的链接进行绑定
  commitsArray.forEach(commit => {
    if (commit.message.startsWith("newfeature:")) {
      features.push(
        `* ${commit.message.replace("newfeature:", "")} ([${commit.sha.substring(
          0,
          6
        )}](https://github.com/wxh0402/DNFCalculating/commit/${
          commit.sha
        }))\n`
      );
    }
    if (commit.message.startsWith("bugfix:")) {
      Bugfixes.push(
        `* ${commit.message.replace("bugfix:", "")} ([${commit.sha.substring(
          0,
          6
        )}](https://github.com/wxh0402/DNFCalculating/commit/${
          commit.sha
        }))\n`
      );
    }
  });
  
  if (features.length) {
    newChangelog += `## NewFeatures\n`;
    features.forEach(feature => {
      newChangelog += feature;
    });
    newChangelog += '\n';
  }
  
  if (Bugfixes.length) {
    newChangelog += `## BugFixes\n`;
    Bugfixes.forEach(bugfix => {
      newChangelog += bugfix;
    });
    newChangelog += '\n';
  }
  if(features.length + Bugfixes.length >0){
  // prepend the newChangelog to the current one
  fs.writeFileSync("./CHANGELOG.md", `${newChangelog}${currentChangelog}`);
  // update package.json
  fs.writeFileSync("./Bulid/release_version.json", JSON.stringify({ version: String(newVersion) }, null, 2));
  
  // create a new commit
  child.execSync('git add .');
  child.execSync(`git commit -m "chore: Bump to  ${newVersion}"`);
  
  // tag the commit
  child.execSync(`git tag -a -m "Tag for ${newVersion}" ${newVersion}`);
  }
}