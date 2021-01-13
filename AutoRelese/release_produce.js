  const child = require("child_process");
  const latestTag = child.execSync('git describe --long').toString('utf-8').split("-");
  const currentVersion = (require("../ResourceFiles/Config/release_version.json").version).toString();
  // const gitVersion = latestTag[0]+'-'+latestTag[1]+'-'+latestTag[2]
  const newVersion = new Date(+new Date() + 8 * 3600 * 1000).toISOString().split("T")[0]
  var date = new Date
  const lastMonth = (date.getMonth() ==0 ? date.getFullYear()-1:date.getFullYear()).toString()+'-'+(date.getMonth() ==0 ? 12 : date.getMonth() ).toString()
  const fs = require("fs");
  
  const output = child
  .execSync(`git log ${currentVersion}..HEAD --format=%B%H----DELIMITER----`)
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
  
  var currentChangelog = fs.readFileSync("docs/CHANGELOG.md", "utf-8");
  
  // 用version和时间作为release 标记
  let newChangelog = `## Newest\n\n### ${
    new Date(+new Date() + 8 * 3600 * 1000).toISOString().split("T")[0]
  }\n\n`;
  
  const features = [];
  const Bugfixes = [];
  
  // 分别维护features和bugfixes的内容，并将message和commit的链接进行绑定
  commitsArray.forEach(commit => {
    if (commit.message.startsWith("new")||commit.message.startsWith("newfeature")) {
      features.push(
        `* ${commit.message.replace(/\n/,"<br>\n").replace("new:", "").replace("new", "").replace("newfeature:", "").replace("<br><br>","<br>")} ([${commit.sha.substring(
          0,
          6
        )}](https://github.com/wxh0402/DNFCalculating/commit/${
          commit.sha
        }))\n`
      );
    }
    if (commit.message.startsWith("bug")||commit.message.startsWith("bugfix")) {
      Bugfixes.push(
        `* ${commit.message.replace(/\n/,"<br>\n").replace("bug:", "").replace("bugfix:", "").replace("bugfix", "").replace("<br><br>","<br>")} ([${commit.sha.substring(
          0,
          6
        )}](https://github.com/wxh0402/DNFCalculating/commit/${
          commit.sha
        }))\n`
      );
    }
  });
  
  if (features.length) {
    newChangelog += `#### NewFeatures\n`;
    features.sort()
    features.forEach(feature => {
      newChangelog += feature;
    });
    newChangelog += '\n';
  }
  
  if (Bugfixes.length) {
    newChangelog += `#### BugFixes\n`;
    Bugfixes.sort()
    Bugfixes.forEach(bugfix => {
      newChangelog += bugfix;
    });
    newChangelog += '\n';
  }
  if(features.length + Bugfixes.length >0){
  // prepend the newChangelog to the current one
  currentChangelog = currentChangelog.replace("## Newest\n\n","")
  currentChangelog = currentChangelog.replace("## History\n\n","")
  var start = currentChangelog.indexOf("### "+lastMonth)
  currentChangelog = currentChangelog.slice(0,start)+"\n## History\n\n"+currentChangelog.slice(start)
  fs.writeFileSync("docs/CHANGELOG.md", `${newChangelog}${currentChangelog}`);
  fs.writeFileSync("ResourceFiles/Config/release_version.json", JSON.stringify({ 
    version: String(newVersion) , 
    AutoCheckUpdate:true,
    // EquipmentVersion:"TYF",
    ShowChangeLog : true,
    // ZFVersion: "TYF"
   }, null, 2));
  // create a new commit
  child.execSync('git add .');
  child.execSync(`git commit -m "chore: Bump to  ${newVersion}"`);
  // // tag the commit
  child.execSync(`git tag -a -m "Tag for ${newVersion}" ${newVersion}`);

  child.execSync(`git push origin --tags`);

  child.execSync(`git push`);
  }
