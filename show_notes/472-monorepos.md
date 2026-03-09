# #472: Monorepos

Sponsored by us! Support our work through:
- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**The Complete pytest Course**](https://courses.pythontest.com/p/the-complete-pytest-course)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)
**Connect with the hosts**
- Michael: [@mkennedy@fosstodon.org](https://fosstodon.org/@mkennedy) / [@mkennedy.codes](https://bsky.app/profile/mkennedy.codes) (bsky)
- Brian: [@brianokken@fosstodon.org](https://fosstodon.org/@brianokken) / [@brianokken.bsky.social](https://bsky.app/profile/brianokken.bsky.social)
- Show: [@pythonbytes@fosstodon.org](https://fosstodon.org/@pythonbytes) / [@pythonbytes.fm](https://bsky.app/profile/pythonbytes.fm) (bsky)
Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually **Monday** at 11am PT. Older video versions available there too.
Finally, if you want an artisanal, hand-crafted digest of every week of the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

**Brian #1: [Setting up a Python monorepo with uv workspaces](https://dev.to/aws/3-things-i-wish-i-knew-before-setting-up-a-uv-workspace-30j6)**

- Dennis Traub
- The 3 things
  - Give the Root a Distinct Name
  - Use workspace = true for Inter-Package Deps
  - Use importlib Mode for pytest

**Michael #2: [cattrs](https://catt.rs/en/stable/): Flexible Object Serialization and Validation**

- **cattrs** is a Swiss Army knife for (un)structuring and validating data in Python.
- A natural alternative/follow on from [DataClass Wizard](https://github.com/rnag/dataclass-wizard)
- Converts to ←→ from dictionaries
- *cattrs* also focuses on **functional composition** and **not coupling** your data model to its serialization and validation rules.
- When you’re handed unstructured data (by your network, file system, database, …), *cattrs* helps to convert this data into trustworthy structured data.
- Batteries Included: cattrs comes with pre-configured converters for a number of serialization libraries, including JSON (standard library, orjson, UltraJSON), msgpack, cbor2, bson, PyYAML, tomlkit and msgspec (supports only JSON at this time).

**Brian #3: [Learning to program in the AI age](https://jblanca.net/edu/learning_programming_in_ai_age/)**

- Jose Blanca
- “I teach a couple of introductory Python courses and I've been thinking about which advice to give to my students, that are studying how to program for the first time. I have collected my ideas in these blog posts”
  - [Why](https://jblanca.net/blog/2026/03/06/learning-to-code-in-the-ai-age/) learning to program is as useful as ever, even with powerful AI tools available.
  - [How](https://jblanca.net/blog/2026/03/07/the-art-of-learning-in-the-ai-age/) to use AI as a tutor rather than a shortcut, and why practice remains the key to real understanding.
  - [What](https://jblanca.net/blog/2026/03/08/programming-what-to-learn/) the real learning objectives are: mental models, managing complexity, and thinking like a software developer.

**Michael #4: [VS Code extension](https://www.linkedin.com/posts/savannahostrowski_hey-you-are-you-using-fastapi-well-activity-7432877782914977793-2ayP/?utm_medium=ios_app&rcm=ACoAAABOjqABPkOWTTbZXV9tmnQohvpkplQOibU&utm_source=social_share_send&utm_campaign=share_via) for FastAPI and friends**

- Enhances the FastAPI development experience in Visual Studio Code
- **Path Operation Explorer**: Provides a hierarchical tree view of all FastAPI routes in your application.
- **Search for routes**: Use the Command Palette and quickly search for routes by path, method, or name.
- **CodeLens links appear above HTTP client calls** like client.get('/items'), letting you jump directly to the matching route definition.
- **Deploy your application** directly to [FastAPI Cloud](https://fastapicloud.com/) from the status bar with zero config.
- View **real-time logs from your FastAPI Cloud** deployed applications directly within VS Code.
- [Install from Marketplace](https://marketplace.visualstudio.com/items?itemName=FastAPILabs.fastapi-vscode).

**Extras**

Brian:
- [Guido van Rossum interviews key Python developers from the first 25 years](https://gvanrossum.github.io/interviews/index.html)
  - [**Interview with Brett Cannon**](https://gvanrossum.github.io/interviews/BrettCannon.html)
  - [**Interview with Thomas Wouters**](https://gvanrossum.github.io/interviews/ThomasWouters.html)
  Michael:
- [IntelliJ IDEA: The Documentary | An origin story](https://www.youtube.com/watch?v=Kourq_Lz03U) video
- Cursor Joined [the ACP Registry](https://www.jetbrains.com/acp/) and Is [Now Live in Your JetBrains IDE](https://blog.jetbrains.com/ai/2026/03/cursor-joined-the-acp-registry-and-is-now-live-in-your-jetbrains-ide/?utm_source=marketo&utm_medium=email&utm_content=blog&utm_campaign=ai&lidx=0&wpid=685326&mkt_tok=NDI2LVFWRC0xMTQAAAGgXJQdteprtfw26Lw-urwLQEjJcm8qYIOseeX-9jODplxTohhXyxl11ZbYr2ehMl__lEyRq0YT8B-mqpzj-fMmOeHXBN0Lz1o9_QOCmx7qSij-fDKY)
- [What hyper-personal software looks like](https://mkennedy.codes/posts/what-hyper-personal-software-looks-like/)
- I’m doing in-person training again (limited scope):
  - [On-site, hands-on AI engineering enablement for software teams with Michael](https://mkennedy.codes/agentic-ai-enablement/)

Joke: [Saas is dead](https://www.reddit.com/r/SaasDevelopers/comments/1rcdzrk/saas_is_dead/?share_id=Zi4lrnVSFkytCUnpfYIMo&utm_content=1&utm_medium=ios_app&utm_name=ioscss&utm_source=share&utm_term=1)

Links

- [Setting up a Python monorepo with uv workspaces](https://dev.to/aws/3-things-i-wish-i-knew-before-setting-up-a-uv-workspace-30j6)
- [cattrs](https://catt.rs/en/stable/)
- [DataClass Wizard](https://github.com/rnag/dataclass-wizard)
- [Learning to program in the AI age](https://jblanca.net/edu/learning_programming_in_ai_age/)
- [Why](https://jblanca.net/blog/2026/03/06/learning-to-code-in-the-ai-age/)
- [How](https://jblanca.net/blog/2026/03/07/the-art-of-learning-in-the-ai-age/)
- [What](https://jblanca.net/blog/2026/03/08/programming-what-to-learn/)
- [VS Code extension](https://www.linkedin.com/posts/savannahostrowski_hey-you-are-you-using-fastapi-well-activity-7432877782914977793-2ayP/?utm_medium=ios_app&rcm=ACoAAABOjqABPkOWTTbZXV9tmnQohvpkplQOibU&utm_source=social_share_send&utm_campaign=share_via)
- [FastAPI Cloud](https://fastapicloud.com/)
- [Install from Marketplace](https://marketplace.visualstudio.com/items?itemName=FastAPILabs.fastapi-vscode)
- [Guido van Rossum interviews key Python developers from the first 25 years](https://gvanrossum.github.io/interviews/index.html)
- [Interview with Brett Cannon](https://gvanrossum.github.io/interviews/BrettCannon.html)
- [Interview with Thomas Wouters](https://gvanrossum.github.io/interviews/ThomasWouters.html)
- [IntelliJ IDEA: The Documentary | An origin story](https://www.youtube.com/watch?v=Kourq_Lz03U)
- [the ACP Registry](https://www.jetbrains.com/acp/)
- [Now Live in Your JetBrains IDE](https://blog.jetbrains.com/ai/2026/03/cursor-joined-the-acp-registry-and-is-now-live-in-your-jetbrains-ide/?utm_source=marketo&utm_medium=email&utm_content=blog&utm_campaign=ai&lidx=0&wpid=685326&mkt_tok=NDI2LVFWRC0xMTQAAAGgXJQdteprtfw26Lw-urwLQEjJcm8qYIOseeX-9jODplxTohhXyxl11ZbYr2ehMl__lEyRq0YT8B-mqpzj-fMmOeHXBN0Lz1o9_QOCmx7qSij-fDKY)
- [What hyper-personal software looks like](https://mkennedy.codes/posts/what-hyper-personal-software-looks-like/)
- [On-site, hands-on AI engineering enablement for software teams with Michael](https://mkennedy.codes/agentic-ai-enablement/)
- [Saas is dead](https://www.reddit.com/r/SaasDevelopers/comments/1rcdzrk/saas_is_dead/?share_id=Zi4lrnVSFkytCUnpfYIMo&utm_content=1&utm_medium=ios_app&utm_name=ioscss&utm_source=share&utm_term=1)
