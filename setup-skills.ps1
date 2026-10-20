# Hunterseek Private Workshop — register the role skills with DSH.
#
# DSH discovers skills in two places:
#   <project>\.dsh\skills\<name>\SKILL.md   — only while a session is open in this folder
#   <DSH_HOME>\skills\<name>\SKILL.md       — every session, whichever folder is open
#
# This script links the six role folders into both, so the crew is available inside the
# workshop and in any other project folder. Each entry is a directory link (junction on
# Windows): the real SKILL.md stays the single source of truth and edits take effect
# immediately with no copy to maintain.
#
# Run once after cloning/moving this folder to a new machine:
#   pwsh -NoProfile -File .\setup-skills.ps1
# Use -ProjectOnly to register only the workshop-local links and keep the crew out of
# other project workspaces. Safe to re-run: good links are left alone, broken ones rebuilt.

param(
    [switch]$ProjectOnly
)

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$roles = @('sam-social', 'vans-video', 'pat-photo', 'mark-music', 'gale-gaming', 'ace-arena')
$dshHome = if ($env:DSH_HOME) { $env:DSH_HOME } else { Join-Path $HOME '.dsh' }
$anchor = '> **Workshop root:** `' + $root + '` — every `memory/...` path in this skill means `<workshop root>\memory\...`, even when the session is open in a different project folder.'

function Register-RoleLinks([string]$skillsDir) {
    New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null
    Write-Host "ROOT  $skillsDir"

    foreach ($role in $roles) {
        $target = Join-Path $root $role
        $link = Join-Path $skillsDir $role

        if (-not (Test-Path (Join-Path $target 'SKILL.md'))) {
            Write-Host "SKIP  $role — no SKILL.md in $target"
            continue
        }

        if (Test-Path $link) {
            if (Test-Path (Join-Path $link 'SKILL.md')) {
                Write-Host "OK    $role — already registered"
                continue
            }
            # A stale or broken entry: remove it before relinking, but only if it is inside
            # the skills folder this call owns.
            $resolved = (Resolve-Path $link).Path
            if (-not $resolved.StartsWith($skillsDir, [StringComparison]::OrdinalIgnoreCase)) {
                throw "Refusing to remove $resolved — outside $skillsDir"
            }
            Remove-Item $link -Recurse -Force
        }

        if ($IsWindows) {
            New-Item -ItemType Junction -Path $link -Target $target | Out-Null
        } else {
            New-Item -ItemType SymbolicLink -Target $target -Path $link | Out-Null
        }

        if (Test-Path (Join-Path $link 'SKILL.md')) {
            Write-Host "LINK  $role -> $target"
        } else {
            Write-Host "FAIL  $role — link could not be created (a copy of SKILL.md also works)"
        }
    }
}

Register-RoleLinks (Join-Path $root '.dsh\skills')
if (-not $ProjectOnly) {
    Register-RoleLinks (Join-Path $dshHome 'skills')
}

# Keep each role's workshop-root note current. Global links mean a role can be loaded from
# an unrelated project folder, where a bare `memory/...` path would otherwise resolve wrong.
$replace = [System.Text.RegularExpressions.MatchEvaluator] { param($m) $anchor }
foreach ($role in $roles) {
    $file = Join-Path $root "$role\SKILL.md"
    if (-not (Test-Path $file)) { continue }
    $text = Get-Content -Raw -LiteralPath $file
    if ($text -match '(?m)^> \*\*Workshop root:\*\*') {
        $text = [regex]::Replace($text, '(?m)^> \*\*Workshop root:\*\*.*$', $replace)
    } else {
        $m = [regex]::Match($text, '(?s)\A(---\r?\n.*?\r?\n---\r?\n)')
        if (-not $m.Success) { Write-Host "WARN  $role — no frontmatter, skipped"; continue }
        $text = $m.Groups[1].Value + "`r`n" + $anchor + "`r`n" + $text.Substring($m.Length)
    }
    Set-Content -LiteralPath $file -Value $text -Encoding utf8NoBOM -NoNewline
}

Write-Host ''
Write-Host 'Done. DSH picks these up without a restart; a fresh session always sees them.'