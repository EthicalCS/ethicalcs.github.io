var repoPath = "https://github.com/ethicalcs/ethicalcs.github.io/";

function getThisPath()
{
    var path = window.location.pathname;
    if (path === "/")
    {
        path = "/index/";
        path = path.slice(0, -1);
    }
    path = path.replace(".html","");
    return path
}

function createPullRequestURL()
{
    return repoPath + "edit/master" + getThisPath() + ".md";
}

function createFileBugURL()
{
    var title = "Fix content problem on " + getThisPath() + ".md";
    return repoPath + "issues/new/?title=" + encodeURIComponent(title);
}

function runMainScript()
{
    $("#file-bug-anchor").attr("href", createFileBugURL());
    $("#pull-request-anchor").attr("href", createPullRequestURL());
}
