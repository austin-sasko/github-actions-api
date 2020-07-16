  
const core = require("@actions/core");
const github = require("@actions/github");

async function run() {
  const issueTitle = core.getInput("issueTitle");
  const issueBody = core.getInput("issueBody");
  const calc_input = core.getInput("calc_input");
  const calc_result = core.getInput("calc_result");

  const token = core.getInput("repoToken");
  try {
    const octokit = new github.GitHub(token);
    issueBody = calc_input + calc_result;
    const newIssue = await octokit.issues.create({
      repo: github.context.repo.repo,
      owner: github.context.repo.owner,
      title: issueTitle,
      body: issueBody
    });
  } catch (error) {
    core.setFailed(error.message);
  }
}

run();
