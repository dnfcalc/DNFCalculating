const child = require("child_process");
const fs = require("fs");

const latestTag = child.execSync('git describe --long').toString('utf-8').split('-')[0];
const output = child
  .execSync(`git log ${latestTag}..HEAD --format=%B%H----DELIMITER----`)
  .toString("utf-8");

// const output = child
//   .execSync(`git log --format=%B%H----DELIMITER----`)
//   .toString("utf-8");

const commitsArray = output
  .split("----DELIMITER----\n")
  .map(commit => {   
    let data = commit.split("\n");
    let returndata = ['',''];
    let i = 0
    for(i;i<data.length-1;i++){
       returndata[0]+=data[i]+(i<data.length-2?'<br>':'')
     }
    const [message, sha] = [returndata[0],data[data.length-1]];
    // let retmessage = "测试"
    // for(let i =0;i<msg.length-1;i++){
    //   retmessage+=msg[i]+i<msg.length-2?'\n':''
    // }
    // let retsha = msg[msg.length-1]
    // const [message, sha] = [retmessage,retsha]
    return {sha, message };
  })
  .filter(commit => Boolean(commit.sha));

const currentChangelog = fs.readFileSync("./CHANGELOG.md", "utf-8");
// const currentVersion = Number(require("./release_version.json").version);


// 用version和时间作为release 标记
var now = new Date();
var year = now.getFullYear(); //得到年份
var month = now.getMonth();//得到月份
var date = now.getDate();//得到日期
month = month + 1;
if (month < 10) month = "0" + month;
if (date < 10) date = "0" + date;
var time = "";
time = year + "." + month + "." + date;
let newChangelog = `# ${
  time
}\n\n`;

const newVersion = time

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

// prepend the newChangelog to the current one
fs.writeFileSync("./CHANGELOG.md", `${newChangelog}${currentChangelog}`);
// update package.json
fs.writeFileSync("./release_version.json", JSON.stringify({ version: String(newVersion) }, null, 2));

// create a new commit
child.execSync('git add .');
child.execSync(`git commit -m "chore: Bump to version ${newVersion}"`);

// tag the commit
child.execSync(`git tag -a -m "Tag for version ${newVersion}" version${newVersion}`);