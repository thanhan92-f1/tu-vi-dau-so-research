# Đăng repository lên GitHub

## Cách 1 — GitHub CLI

Tại thư mục `tu-vi-dau-so-research`:

```bash
git init
git add .
git commit -m "feat: initial Tử Vi Đẩu Số research skill"
git branch -M main
gh repo create thanhan-92f1/tu-vi-dau-so-research \
  --public \
  --source=. \
  --remote=origin \
  --push \
  --description "Agent Skill nghiên cứu và luận giải Tử Vi Đẩu Số Việt Nam có đối chiếu, phản chứng và nghiệm lý"
```

## Cách 2 — Tạo repo trên giao diện GitHub

1. Tạo repository mới tên `tu-vi-dau-so-research`.
2. Không tạo sẵn README, `.gitignore` hoặc license vì bộ này đã có.
3. Chạy:

```bash
git init
git add .
git commit -m "feat: initial Tử Vi Đẩu Số research skill"
git branch -M main
git remote add origin https://github.com/thanhan92-f1/tu-vi-dau-so-research.git
git push -u origin main
```

## Topics đề xuất

```text
agent-skills, skill-md, claude-code, ai-agent, vietnamese, tu-vi, zi-wei-dou-shu, astrology-research, prompt-engineering
```

## Release đầu tiên

Tạo tag:

```bash
git tag -a v1.0.0 -m "Tử Vi Đẩu Số Research Skill v1.0.0"
git push origin v1.0.0
```

Trong GitHub Releases, tải lên file ZIP đóng gói và dùng nội dung trong `CHANGELOG.md` làm release notes.
