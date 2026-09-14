# DevOps & Platform Engineering Examples

Runnable configuration and scripting for the delivery pipeline: CI/CD, container
builds, Kubernetes workloads, infrastructure as code, configuration management,
observability, and operational scripts.

## Layout

| Directory | Tooling | Files |
|:---|:---|:---|
| `ci/github_actions/` | GitHub Actions | CI, matrix builds, CD, release automation, CodeQL, Docker publish, reusable workflows |
| `ci/gitlab/` | GitLab CI | pipeline stages, manual deploy, per-MR review apps |
| `ci/jenkins/` | Jenkins | declarative pipeline, multibranch, shared library |
| `docker/` | Docker | Node/Python/Go images, multi-stage and distroless builds, Compose (prod + dev), `.dockerignore` |
| `kubernetes/` | Kubernetes | Deployment, Service, ConfigMap, Secret, Ingress, HPA, StatefulSet, DaemonSet, Job/CronJob, RBAC, NetworkPolicy, PDB, probes |
| `terraform/` | Terraform | provider/backend, variables, outputs, VPC, EC2, S3 + ALB |
| `ansible/` | Ansible | playbook, inventory, group vars, `common` and `nginx` roles |
| `helm/` | Helm | chart metadata, values, templated Deployment/Service/HPA and helpers |
| `monitoring/` | Prometheus/Grafana/OTel | scrape config, alert rules, Loki, Grafana dashboard, OTel collector, blackbox probes |
| `scripts/` | Bash | deploy, backup, healthcheck, rolling restart, log rotation |
| `make/` | GNU Make | app build tasks, Python venv tasks, self-documenting task runner |

## Validation

```bash
# YAML (workflows, manifests, playbooks, monitoring)
python3 -c "import glob, yaml; [list(yaml.safe_load_all(open(f))) for f in glob.glob('devops/**/*.yml', recursive=True)]"

# Shell scripts
for f in devops/scripts/*.sh; do bash -n "$f"; done

# Makefiles
make -f devops/make/Makefile help
make -f devops/make/Makefile.tasks help
```

`make test-devops` runs the YAML and shell checks from the repository root.

## Conventions

- Manifests default to production-safe settings: resource requests/limits,
  non-root users, read-only where possible, and least-privilege RBAC.
- Images are pinned by digest or explicit tag and built reproducibly with
  multi-stage Dockerfiles and build caches.
- Secrets are referenced from a secret manager (for example the External
  Secrets Operator) rather than committed as literals.
