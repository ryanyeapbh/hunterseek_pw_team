# Hunterseek Private Workshop — register the four role skills with DSH.
#
# DSH discovers skills at <project>\.dsh\skills\<name>\SKILL.md. The role folders live one
# level up, so each entry here is a directory link (junction) — the real SKILL.md stays the
# single source of truth, and edits take effect immediately.
#
# Run once after cloning/moving this folder to a new machine:
#   pwsh -NoProfile -File .\setup-skills.ps1
#
# Safe to re-run: existing links are left alone, broken ones are rebuilt.

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$skillsDir = Join-Path $root '.dsh\skills'
$roles = @('sam-social', 'vans-video', 'pat-photo', 'mark-music', 'gale-gaming')

New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null

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
        # this workshop's .dsh\skills folder.
        $resolved = (Resolve-Path $link).Path
        if (-not $resolved.StartsWith($skillsDir, [StringComparison]::OrdinalIgnoreCase)) {
            throw "Refusing to remove $resolved — outside $skillsDir"
        }
        Remove-Item $link -Recurse -Force
    }

    if ($IsWindows) {
        cmd /c mklink /J "$link" "$target" | Out-Null
    } else {
        New-Item -ItemType SymbolicLink -Target $target -Path $link | Out-Null
    }

    if (Test-Path (Join-Path $link 'SKILL.md')) {
        Write-Host "LINK  $role -> $target"
    } else {
        Write-Host "FAIL  $role — link could not be created (a copy of SKILL.md also works)"
    }
}

Write-Host ''
Write-Host 'Done. DSH picks these up without a restart; a fresh session always sees them.'
