# Hunterseek Private Workshop — GitHub auto-sync.
#
# Stages everything, commits only when something actually changed, then pushes to the
# remote configured as `origin` (currently https://github.com/ryanyeapbh/hunterseek_pw_team,
# private).
#
# Runs unattended from Windows Task Scheduler ("Hunterseek GitHub sync", daily 21:00,
# catch-up enabled). Safe to run by hand any time:  pwsh -NoProfile -File .\sync-github.ps1
#
# Logs to %LOCALAPPDATA%\hunterseek-pw\sync.log (outside the repo, so logging never
# creates commits). Credentials are never stored here — Git Credential Manager holds them.

$ErrorActionPreference = 'Stop'

$repo = $PSScriptRoot
$branch = 'main'
$logDir = Join-Path $env:LOCALAPPDATA 'hunterseek-pw'
$logFile = Join-Path $logDir 'sync.log'
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Write-Log([string]$Message) {
    $line = "{0}  {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Message
    Add-Content -Path $logFile -Value $line -Encoding utf8
    Write-Host $line
}

# Unattended: never block waiting for a credential prompt or terminal input.
$env:GIT_TERMINAL_PROMPT = '0'
$env:GCM_INTERACTIVE = 'never'

try {
    Set-Location $repo

    if (-not (Test-Path (Join-Path $repo '.git'))) {
        Write-Log 'SKIP  no .git repository at this path'
        exit 1
    }

    $dirty = git status --porcelain
    if ($dirty) {
        git add -A
        $staged = git diff --cached --name-only
        if ($staged) {
            $summary = ($staged -split "`n" | Select-Object -First 6) -join ', '
            if (($staged -split "`n").Count -gt 6) { $summary += ", ..." }
            git commit -q -m ("Auto-sync {0}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm'))
            Write-Log "COMMIT  $summary"
        }
    }

    # Push. If the remote moved ahead (edited on GitHub, another machine), rebase once.
    git push -q origin $branch 2>&1 | Out-String | ForEach-Object {
        if ($_.Trim()) { Write-Log "PUSH-OUT  $($_.Trim())" }
    }
    if ($LASTEXITCODE -ne 0) {
        Write-Log 'PUSH  rejected or failed — trying pull --rebase --autostash'
        git pull --rebase --autostash -q origin $branch 2>&1 | Out-Null
        if ($LASTEXITCODE -ne 0) {
            git rebase --abort 2>$null | Out-Null
            Write-Log 'ERROR  rebase conflict — resolve by hand, nothing was pushed'
            exit 1
        }
        git push -q origin $branch 2>&1 | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Log 'ERROR  push still failed after rebase (check credentials/network)'
            exit 1
        }
        Write-Log 'PUSH    rebased and pushed'
    } else {
        Write-Log 'PUSH    ok (nothing to send or up to date)'
    }

    $head = git log --oneline -1
    Write-Log "HEAD    $head"
    exit 0
}
catch {
    Write-Log "ERROR  $($_.Exception.Message)"
    exit 1
}
