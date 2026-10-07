<a href="https://contact-shubham.vercel.app/">
  <img src="./assets/hero.svg" width="100%" alt="Terminal: Shubham Chauhan, senior software engineer, full stack" />
</a>

<p align="center">
  <a href="https://contact-shubham.vercel.app/"><img src="https://img.shields.io/badge/portfolio-contact--shubham-0d1117?style=for-the-badge&logo=vercel&logoColor=white&labelColor=0d1117&color=1f6feb" alt="Portfolio" /></a>
  <a href="https://linkedin.com/in/itshubham"><img src="https://img.shields.io/badge/linkedin-itshubham-0d1117?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0d1117&color=0a66c2" alt="LinkedIn" /></a>
  <a href="mailto:dev2shubham@gmail.com"><img src="https://img.shields.io/badge/email-dev2shubham-0d1117?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0d1117&color=ea4335" alt="Email" /></a>
  <a href="https://x.com/contactshubham"><img src="https://img.shields.io/badge/x-contactshubham-0d1117?style=for-the-badge&logo=x&logoColor=white&labelColor=0d1117&color=30363d" alt="X" /></a>
  <img src="https://komarev.com/ghpvc/?username=heyitshubham&label=views&color=3fb950&style=for-the-badge&labelColor=0d1117" alt="Profile views" />
</p>

<p align="center"><i>"Anything, but not everything."</i></p>

## `$ cat application.yml`

```yaml
shubham:
  role: senior software engineer · full stack
  based-in: delhi ncr, india
  day-job: qss technosoft            # since 2022, key contributor 2025
  ships: [spring boot apis, angular uis, releases on aws + gcp]
  favourite-bug: the one that only happens in a US time zone
  superpower: finding why a system is slow   # unused index, blocked thread, missing cache
  learning: [java 21 virtual threads, ai agents, aws solutions architect]
  off-duty: table tennis 🏓
  open-to: interesting backend problems, talks, hackathons
```

## 🎤 On stage

<a href="https://github.com/heyitshubham/pr-review-skill">
  <img src="./assets/talk.svg" width="100%" alt="DevFest Noida 2026 talk: AI writes your code. Who checks it?" />
</a>

## 🏗️ Biggest thing I've built at work

<img src="./assets/architecture.svg" width="100%" alt="A legacy monolith split into nine Spring Boot microservices behind an API gateway, over Kafka and Amazon SQS" />

<details>
<summary><b>🐛 Bug journal: production problems I've tracked down</b> (click to open)</summary>
<br />

| Symptom | Real cause | Fix |
|---|---|---|
| Order search read **every row** | Search terms were passed as an array, which a `GIN (pg_trgm)` index can't use | Rewrote the condition so all three indexes were used again: **full table scan → index lookup** |
| Shared service code **froze under load** | Deadlock between threads | Found the deadlock and moved the work from one-at-a-time to parallel |
| Bugs only **US customers** saw | Failures depended on **time zone and locale** | Recreated the customer environment locally; supported releases in US hours |
| Bulk product enrichment **held up releases** | One record processed at a time | `ExecutorService` + `CompletableFuture`, thread-safe with `AtomicInteger` |
| Kiosk queue screens **showed stale data** | Client-side GraphQL cache | Turned off Apollo caching for live queues so the screen always matches the room |
| Angular v9 upgrade **"too risky to try"** | Nine major versions behind | Upgraded **v9 → v20** one version at a time, moved 30+ modules to standalone, **no downtime** |

</details>

## 🚀 Things I build after hours

<table>
  <tr>
    <td width="50%"><a href="https://github.com/heyitshubham/LeadLoop"><img src="./assets/card-leadloop.svg" width="100%" alt="LeadLoop: an AI agent with a human approving every email" /></a></td>
    <td width="50%"><a href="https://github.com/heyitshubham/dukaan-saathi"><img src="./assets/card-dukaan-saathi.svg" width="100%" alt="Dukaan Saathi: an AI business partner for kirana stores" /></a></td>
  </tr>
  <tr>
    <td width="50%"><a href="https://github.com/heyitshubham/pr-review-skill"><img src="./assets/card-pr-review-skill.svg" width="100%" alt="pr-review-skill: an Agent Skill that reviews Spring Boot pull requests" /></a></td>
    <td width="50%"><a href="https://github.com/heyitshubham/type-tank-game"><img src="./assets/card-type-tank.svg" width="100%" alt="TYPE//TANK: a retro DOS typing-defense game" /></a></td>
  </tr>
</table>

## 🧰 Toolbox

| | |
|---|---|
| **Backend** | <img src="https://skillicons.dev/icons?i=java,spring,python,fastapi,graphql,maven&theme=dark" height="40" alt="Java, Spring, Python, FastAPI, GraphQL, Maven" /> |
| **Frontend** | <img src="https://skillicons.dev/icons?i=angular,ts,react,nextjs,tailwind,figma&theme=dark" height="40" alt="Angular, TypeScript, React, Next.js, Tailwind, Figma" /> |
| **Data & messaging** | <img src="https://skillicons.dev/icons?i=postgres,mysql,redis,kafka&theme=dark" height="40" alt="PostgreSQL, MySQL, Redis, Kafka" /> |
| **Cloud & delivery** | <img src="https://skillicons.dev/icons?i=aws,gcp,docker,kubernetes,githubactions,gitlab,jenkins&theme=dark" height="40" alt="AWS, GCP, Docker, Kubernetes, GitHub Actions, GitLab, Jenkins" /> |
| **AI-assisted dev** | `Claude Code` · `MCP` · `Agent Skills` · `Cursor` · `LangGraph` |

## 🏆 Trophy shelf

| | |
|---|---|
| 🥇 | **Key Contributor 2025**, QSS Technosoft, for technical leadership and mentoring |
| 🎤 | **Speaker**, DevFest Noida 2026: *"AI Writes Your Code. Who Checks It?"* |
| 🏅 | **7th place**, Smart India Hackathon 2022, as backend team lead |
| 🥇 | **1st place**, Pitch-a-Biz business prototype competition, as technical lead |
| ⚔️ | Built for **SerpApi India Hackathon 2026** and **Paytm Hackathon** (2026) |
| ☁️ | **AWS Certified Solutions Architect – Associate**, in progress |

## 🐍 Contributions, eaten

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/heyitshubham/heyitshubham/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/heyitshubham/heyitshubham/output/github-snake.svg" />
  <img alt="Snake eating my contribution graph" src="https://raw.githubusercontent.com/heyitshubham/heyitshubham/output/github-snake-dark.svg" width="100%" />
</picture>

<p align="center">
  <code>➜ ~ exit</code> &nbsp;·&nbsp; thanks for scrolling this far. Say hi at <a href="mailto:dev2shubham@gmail.com">dev2shubham@gmail.com</a> 👋
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1f6feb,100:3fb950&height=110&section=footer" width="100%" alt="" />
