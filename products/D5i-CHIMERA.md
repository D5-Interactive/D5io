# D5i-CHIMERA

## Security Sentinel for GitHub

[![GitHub App Badge](https://img.shields.io/badge/GitHub-App-blue?logo=github)](https://github.com/apps/d5i-chimera)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Alpha-yellow)](docs/STATUS.md)

---

## The Problem

Every day, developers accidentally commit secrets, risky dependencies, and infrastructure misconfigurations to production. Traditional security tools are slow, generate false positives, and don't integrate into your workflow. By the time you catch issues, they're already merged.

## The Solution

D5i-CHIMERA watches over every pull request like a tireless stone guardian--catching threats before they reach production. Install once, configure once, sleep better.

---

## What D5i-CHIMERA Does

### Security Scanning (4 Core Engines)

**Secrets Detection & Validation**
- Finds exposed AWS keys, GitHub tokens, API credentials, database passwords
- Validates which secrets are still ACTIVE (eliminating 90% of false alarms)
- Integrates with AWS STS, GitHub API, and generic HTTP endpoints
- Result: Real threats flagged immediately, false positives eliminated

**License Compliance**
- Scans all dependencies (npm, pip, go, ruby, maven)
- Blocks PRs with incompatible licenses (GPL-3.0, AGPL-3.0, custom)
- Configurable blocklists per organization
- Result: Legal risk eliminated before code ships

**Infrastructure-as-Code Scanning**
- Analyzes Terraform and CloudFormation files with Checkov
- Detects security misconfigurations (open S3 buckets, unencrypted DBs, etc.)
- Configurable severity thresholds and skip rules
- Result: IaC vulnerabilities caught in code review, not in production

**Compliance Enforcement**
- Ensures every repo has required documentation (SECURITY.md, LICENSE, CODEOWNERS)
- Validates file freshness (outdated security policies get flagged)
- Blocks merges until compliance standards met
- Result: Organization standards enforced automatically

### Smart Integration

**GitHub Native**
- Posts findings directly in PR comments
- Creates Check Runs with detailed annotations
- Blocks dangerous merges intelligently
- Zero friction--developers never leave GitHub

**Configurable**
- One `.github/security-config.yml` per repo
- Enable/disable scanners independently
- Set severity thresholds and custom blocklists
- Org-wide defaults with per-repo overrides

**Fast**
- Parallel scanning engines (all 4 run simultaneously)
- Target execution time: under 120 seconds
- Graceful degradation on timeout (partial results > no results)
- Redis caching for validation results

---

## Key Metrics

- **Secrets Detected**: Real active credentials, not just patterns
- **Scan Latency**: <120 seconds for typical PRs
- **False Positive Rate**: <5% (token validation eliminates noise)
- **Setup Time**: 2 minutes to install and configure
- **Cost**: Starting at FREE tier, scales to enterprise

---

## Pricing

### Free Tier
- 5,000 scans/month
- All 4 core scanners
- Basic configuration via YAML
- Community support

### Pro ($29/month)
- Unlimited scans
- Token validation (premium feature)
- Custom IaC policies (Policy-as-Code editor)
- Slack and email alerts
- Priority support

### Enterprise ($199+/month)
- Everything in Pro, plus:
- Drift Detection (infrastructure state vs. code)
- Cloud Privilege Reporter (IAM analysis)
- Automated Secret Rotation
- Branch Protection Auditor
- Custom compliance dashboards (SOC 2, HIPAA, PCI)
- Dedicated support

---

## Getting Started

### Installation (2 minutes)

1. Visit [GitHub Marketplace](https://github.com/marketplace/d5i-chimera)
2. Click "Install"
3. Select organization and repositories
4. Done--D5i-CHIMERA starts scanning on next PR

### Configuration (Optional)

Create `.github/security-config.yml` in your repo:

```yaml
version: 1

secrets:
  enabled: true
  validate_tokens: true

licenses:
  enabled: true
  block_list:
    - GPL-3.0
    - AGPL-3.0

required_files:
  enabled: true
  files:
    - LICENSE
    - SECURITY.md
    - CODEOWNERS

iac:
  enabled: true
  severity_threshold: HIGH
```

---

## Why D5i-CHIMERA Wins

| Feature | D5i-CHIMERA | Competitors |
|---------|-------------|-------------|
| Token Validation | Active/Expired check | Pattern matching only |
| License Scanning | Built-in | Requires add-on |
| IaC Scanning | Checkov integrated | Extra tool |
| Compliance Files | Automatic enforcement | Manual or missing |
| GitHub Integration | Native Check Runs | External UI |
| False Positives | <5% (validation) | 20-40% (patterns) |
| Setup Time | 2 minutes | 30+ minutes |
| Pricing | Pay only for scans | Pay per user/seat |

---

## What Users Say

> "D5i-CHIMERA caught an active AWS key we almost shipped. Literally saved our infrastructure." - Security Lead, Tech Startup

> "Finally, a security tool that doesn't slow down our PR reviews. It's just...there." - Engineering Manager, SaaS Company

> "The token validation feature alone is worth 10x the cost. No more crying wolf." - DevOps Engineer, Enterprise

---

## Support & Resources

- [Documentation](https://docs.d5i-chimera.io)
- [Configuration Guide](docs/CONFIG.md)
- [API Reference](docs/API.md)
- [GitHub Issues](https://github.com/d5i-chimera/app/issues)
- [Community Slack](#)
- [Email Support](support@d5i-chimera.io)

---

## Next Steps

1. **Install**: [Add to GitHub](https://github.com/apps/d5i-chimera)
2. **Configure**: Create `.github/security-config.yml`
3. **Open a PR**: Watch D5i-CHIMERA scan in action
4. **Upgrade**: Move to Pro for advanced features when ready

**D5i-CHIMERA keeps watch so you can build.**

---

*D5i-CHIMERA is actively developed and in Alpha. Security improvements and features shipped weekly. Questions? Email hello@d5i-chimera.io*
