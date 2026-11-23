# <img src="assets/rover.svg" width="66" alt="" /> Ahmed Abdelghafar Mohamed

I study computer science at The Egyptian Chinese University. I built an offline planner because I wanted my timetable, notes, and deadlines in one place. My latest project takes a small detour from campus to Mars.

[LinkedIn](https://www.linkedin.com/in/ahmed-el-zoghby-8320ab278) · [Email](mailto:zoghby2007@gmail.com) · [Meet our robot ↓](#interactive-mobile-robot) · [Browse my repositories](https://github.com/zoghby-ctrl?tab=repositories)

## 🛰️ Latest build · Marswalk

<a href="https://github.com/zoghby-ctrl/zoghby-ctrl/blob/main/assets/jezero-relief.stl">
  <picture>
    <source media="(prefers-reduced-motion: no-preference)" srcset="https://raw.githubusercontent.com/zoghby-ctrl/zoghby-ctrl/main/assets/jezero-orbit.webp">
    <img src="assets/jezero-relief.png" alt="3D relief of Jezero’s western delta. A mint line traces the planned route from Butler landing (A) to the sol 1100 site (B). Open the terrain model.">
  </picture>
</a>

**[Rotate the terrain in 3D ↗](https://github.com/zoghby-ctrl/zoghby-ctrl/blob/main/assets/jezero-relief.stl)** · [Download the textured model (.glb)](https://github.com/zoghby-ctrl/zoghby-ctrl/raw/refs/heads/main/assets/marswalk.glb) · [Plan your own traverse ↗](https://zoghby-ctrl.github.io/quantumions-martian-map/) · [Source code](https://github.com/zoghby-ctrl/quantumions-martian-map)

**Would you take the longer way across Mars to avoid a steep climb?** My teammate and I built Marswalk as Team Quantumions for NASA Space Apps 2026. The mint line follows our planner’s default A* route between two Perseverance sites. It covers **9.55 km** and climbs **234 m**. Change the slope penalty in the planner and compare paths.

<sub>Relief from MGS/MOLA elevations (NASA GSFC and the MOLA Science Team), with colorized MRO/CTX imagery (NASA, JPL-Caltech, MSSS, and USGS Astrogeology). Heights are exaggerated 5×. <a href="https://zoghby-ctrl.github.io/quantumions-martian-map/#sources">Mission data and sources ↗</a></sub>

## On Earth

### Interactive mobile robot

<a href="https://github.com/zoghby-ctrl/zoghby-ctrl/blob/main/assets/mobile-robot.stl">
  <picture>
    <source media="(prefers-reduced-motion: no-preference)" srcset="https://raw.githubusercontent.com/zoghby-ctrl/zoghby-ctrl/main/assets/mobile-robot.webp">
    <img src="assets/mobile-robot.png" alt="Concept model of our four-wheel robot with an ivory shell, OLED smile, camera, and two short gesture paddles. Open the 3D model.">
  </picture>
</a>

For our Computer Architecture project, my team is designing a mobile robot that can turn toward you and wave. Two servos aim the head, and each paddle has a servo of its own. The planned head carries a camera, microphone, and 2.42-inch OLED. The rangefinder sits low on the four-wheel chassis.

This concept animation shows the greeting we're designing. **[Rotate the model ↗](https://github.com/zoghby-ctrl/zoghby-ctrl/blob/main/assets/mobile-robot.stl)** · [Download the animated GLB](https://github.com/zoghby-ctrl/zoghby-ctrl/raw/refs/heads/main/assets/mobile-robot.glb)

### 🎓 Semester OS

Upload a timetable and turn it into a weekly schedule with rooms, notes, and deadlines. I built it with ECU students in mind. Even the OCR runs in the browser, so your timetable stays on your device.

`TypeScript` `IndexedDB` · [Try the demo semester ↗](https://semester-os-4y6.pages.dev/) · [Source](https://github.com/zoghby-ctrl/semester-os)

<details>
<summary>See a day in the demo semester</summary>

![Semester OS Today view with the next class, weekly schedule, and study progress.](https://raw.githubusercontent.com/zoghby-ctrl/semester-os/bfbc1e5be38a4ed01d51372d77439bb68024f6c3/docs/screenshots/01-today-prism.png)

</details>

### 🚑 Q-Rescue

The shortest predicted trip can still miss a deadline. For my Quantum AI course, I built a research tool that lets you compare candidate emergency routes under uncertain travel times. It runs an exact classical solver and a simulated quantum optimizer on the same choices so you can inspect where they agree.

`Python` `PennyLane` `Streamlit` · [Explore the research and results ↗](https://github.com/zoghby-ctrl/Q-Rescue)

<details>
<summary>See the route comparison console</summary>

![Q-Rescue decision console with a synthetic road grid, a deadline control, and the classical-to-quantum processing steps.](https://raw.githubusercontent.com/zoghby-ctrl/Q-Rescue/dba597a1aaa3075c1334a1bce7cc965c151f1d22/output/playwright/final-polish-desktop.png)

</details>

### 🔌 Circuit Copilot

Wire a circuit on a canvas, flip its inputs, and export an Arduino or ESP32 sketch. A browser agent can place components and connect pins on the same canvas you’re looking at.

`TypeScript` `React Flow` `WebMCP` · [Open the canvas ↗](https://circuit-copilot.vercel.app/) · [Source](https://github.com/zoghby-ctrl/Circuit-Copilot)

<details>
<summary>See a one-bit half adder on the canvas</summary>

![Circuit Copilot running its half-adder demo with DIP switches, XOR and AND gates, and two output LEDs.](assets/circuit-canvas.png)

</details>

<details>
<summary><strong>More builds · developer tools, city maps, and a game of Pong</strong></summary>

- **[Forge](https://github.com/zoghby-ctrl/Forge)** records the reasoning behind a pull request alongside the diff that supports it. [Open Forge ↗](https://forge-woad-eight.vercel.app/)
- **[Converge](https://github.com/zoghby-ctrl/Converge)** helps inspection teams spot when several urban incident reports come from the same observation. [Explore the map ↗](https://converge-uni-bud.vercel.app/)
- **[Multiplayer Pong](https://github.com/zoghby-ctrl/Multiplayer-Pong-CPP)** is a team-built C++ game. Two clients share a ball over LAN using Win32 sockets and OpenGL.
- **[Smart Assistant Cane](https://github.com/zoghby-ctrl/AI-Smart-Assistant-Cane)** uses an ESP32 and ultrasonic sensors to warn when an obstacle is getting closer.

</details>

## GitHub activity

<!-- stats:start -->
**333** contributions in the past year · **16** public repositories · **3** stars across original public repositories · **40** followers

<sub>Updated November 23, 2026 · Refreshes weekly</sub>
<!-- stats:end -->
