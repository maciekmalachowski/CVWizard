 <p align="center">
    <img src="frontend/public/wizard.png" align="center" width="20%">
</p>
<p align="center"><h1 align="center">CVWIZARD</h1></p>
<p align="center">
	<em>Craft Your CV, Unlock Your Career Potential</em>
</p>

<p align="center">Built with the tools and technologies:</p>
<p align="center">
	<img src="https://img.shields.io/badge/ChatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white" alt="Openai">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white" alt="Flask">
  <br>
	<img src="https://img.shields.io/badge/React-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB" alt="React">
  	<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="JavaScript">
	<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=for-the-badge&logo=TypeScript&logoColor=white" alt="TypeScript">
	<img src="https://img.shields.io/badge/Tailwind%20CSS-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind">

</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
- [🎗 License](#-license)

---

## 📍 Overview

CVWizard is an innovative web application designed to enhance job application success by aligning CVs with specific job descriptions. Utilizing AI-driven analysis, it extracts and compares skills from uploaded CVs against job requirements, offering tailored advice for optimization. Ideal for job seekers aiming to boost their marketability, CVWizard simplifies the process of tailoring resumes to meet targeted job criteria effectively.

---

## 👾 Features

|      | Feature        | Summary       |
| :--- | :---:         | :---          |
| ⚙️  | **Architecture**  | <ul><li>Modern **client-server architecture** with clear separation of frontend and backend responsibilities.</li><li>Backend powered by `<Python>` and `<Flask>` for API services, CV processing, and AI insights generation.</li><li>Frontend built using `<React>`, `<TypeScript>`, and `<TailwindCSS>` for dynamic and responsive user interfaces.</li></ul> |
| 🤖 | **AI-Powered Insights** | <ul><li>Utilizes **OpenAI** (`gpt-4-turbo`) model via `<LlamaIndex>` to extract **key skills, languages**, and generate **CV summary**.</li><li>Embeds CV data with **OpenAI Embeddings** (`text-embedding-3-large`) for enhanced semantic search and comparison.</li><li>Automatically matches **CV data** against job requirements and generates **AI-powered improvement suggestions**.</li></ul> |
| 📄 | **CV Processing**  | <ul><li>CV content extracted using `<Docling>` library for **PDF text parsing and segmentation**.</li><li>CV data embedded with **OpenAI** to enable semantic search queries.</li><li>Extracts **key skills, languages**, and **experience summary** from CV text.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Frontend developed with `<TypeScript>` for enhanced type safety and maintainability.</li><li>Linting and formatting enforced using `<ESLint>` and `<Prettier>` with best practices for React.</li><li>Backend follows **modular design patterns**, making code easy to extend and maintain.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Seamlessly integrates with **OpenAI API** for embeddings and language model-based insights.</li><li>Job data extracted via **web scraping** using `<BeautifulSoup>`.</li><li>Frontend API communication handled with `<Axios>` for HTTP requests.</li><li>Built and optimized with `<Vite>` for fast and lightweight frontend performance.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Backend code organized into **independent modules**: `<cv_reader>`, `<scrapper>`, and `<ai_insights>`.</li><li>Frontend components are **reusable and isolated**, including `<AnalysisResults>` and `<LoadingState>`.</li><li>Business logic and UI layers are strictly separated for **clean architecture**.</li></ul> |
| 🔍 | **Job-CV Matching** | <ul><li>Automatically identifies **matched and missing keywords** between job descriptions and CVs.</li><li>Provides **AI-generated suggestions** to improve CV alignment with job requirements.</li><li>Visualizes CV-job alignment score with an **interactive radial chart**.</li></ul> |
| 🌐 | **Cross-Origin Support** | <ul><li>Backend secured with **CORS policy** to allow cross-origin API requests from frontend clients.</li><li>Backend supports **JSON-based API responses** for seamless data exchange.</li></ul> |

---

## 📁 Project Structure

```sh
└── CVWizard/
    ├── LICENSE
    ├── README.md
    ├── backend
    │   ├── ai_insights.py
    │   ├── app.py
    │   ├── cv_reader.py
    │   └── scrapper.py
    ├── frontend
    │   ├── .gitignore
    │   ├── README.md
    │   ├── eslint.config.js
    │   ├── index.html
    │   ├── package-lock.json
    │   ├── package.json
    │   ├── postcss.config.js
    │   ├── public
    │   │   └── wizard.png
    │   ├── src
    │   │   ├── App.tsx
    │   │   ├── components
    │   │   │   ├── AnalysisResults.tsx
    │   │   │   └── LoadingState.tsx
    │   │   ├── index.css
    │   │   ├── main.tsx
    │   │   ├── services
    │   │   │   └── api.ts
    │   │   └── vite-env.d.ts
    │   ├── tailwind.config.js
    │   ├── tsconfig.app.json
    │   ├── tsconfig.json
    │   ├── tsconfig.node.json
    │   └── vite.config.ts
    └── requirements.txt
```

### 📂 Project Index
<details open>
	<summary><b><code>CVWIZARD/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- Manages the dependencies essential for the project's operation, ensuring compatibility and functionality across various modules<br>- It includes libraries for web framework capabilities, cross-origin resource sharing, and specialized tools for indexing and experimental features related to llama data processing<br>- This setup is crucial for maintaining the project's architecture and facilitating future enhancements or integrations.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- backend Submodule -->
		<summary><b>backend</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/backend/app.py'>app.py</a></b></td>
				<td>- Backend/app.py serves as the server-side interface for a web application, handling file uploads, data extraction, and AI-driven analysis<br>- It processes uploaded CVs, extracts relevant information, scrapes job data from URLs, and generates insights by comparing CVs with job descriptions, facilitating a comprehensive interaction between the frontend and backend components.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/backend/scrapper.py'>scrapper.py</a></b></td>
				<td>- Scrapes and structures job-related data from specified URLs using BeautifulSoup and requests libraries in Python<br>- It extracts job titles, required skills, and detailed descriptions from web pages, normalizes text spacing, and handles potential errors during the scraping process, returning structured job data or error information as needed.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/backend/ai_insights.py'>ai_insights.py</a></b></td>
				<td>- Generates AI-powered insights for tailoring CVs to specific job descriptions by comparing candidate skills with job requirements<br>- It utilizes an AI model to provide structured feedback, highlighting key areas for improvement and suggesting ways to enhance CV alignment with job skills, ultimately offering personalized advice to candidates.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/backend/cv_reader.py'>cv_reader.py</a></b></td>
				<td>- Processes and indexes curriculum vitae (CV) data by leveraging a document reader, a Markdown parser, and an OpenAI embedding model<br>- It extracts structured information such as skills, languages, and professional summaries from the indexed data, outputting the results in a structured JSON format.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- frontend Submodule -->
		<summary><b>frontend</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/postcss.config.js'>postcss.config.js</a></b></td>
				<td>- Configures PostCSS to use TailwindCSS and Autoprefixer plugins, enhancing the CSS build process for the frontend<br>- TailwindCSS facilitates utility-first styling, while Autoprefixer ensures CSS compatibility across different browsers<br>- This setup is crucial for maintaining a streamlined, responsive design across the project's frontend architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/tsconfig.node.json'>tsconfig.node.json</a></b></td>
				<td>- Configures TypeScript compiler options for the frontend's node environment, focusing on modern JavaScript standards and strict type-checking to enhance code quality and maintainability<br>- It specifically targets the setup for the Vite configuration file, ensuring efficient module resolution and error management during development without outputting compiled files.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/package-lock.json'>package-lock.json</a></b></td>
				<td>- The `package-lock.json` file located in the `frontend` directory plays a crucial role in the overall architecture of the project by ensuring consistent installations and version control of the frontend dependencies<br>- This file lists specific versions of libraries such as React, Axios, and other UI-related packages that are essential for the frontend application's functionality<br>- By locking down these versions, the file prevents discrepancies between development environments and ensures that all developers and deployment pipelines use the exact same versions of each package, thereby avoiding potential conflicts and bugs that could arise from version mismatches<br>- This contributes to the stability and reliability of the frontend codebase within the larger project ecosystem.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/tsconfig.json'>tsconfig.json</a></b></td>
				<td>- Manages TypeScript configuration inheritance within the frontend module by referencing specific configurations for application and node environments<br>- It centralizes TypeScript settings, ensuring consistent compiler behavior across different parts of the frontend development environment, thereby streamlining the build process and maintenance of the codebase.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/tailwind.config.js'>tailwind.config.js</a></b></td>
				<td>- Configures Tailwind CSS for the frontend, specifying which HTML and JavaScript files should utilize Tailwind's utility classes<br>- It sets up the basic theming structure and declares no additional plugins<br>- This configuration ensures that the styling framework is optimized for the project's specific frontend architecture, enhancing UI consistency and performance.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/tsconfig.app.json'>tsconfig.app.json</a></b></td>
				<td>- Configures TypeScript compiler options for the frontend application, targeting modern JavaScript features and optimizing for React JSX<br>- It enhances code quality and maintainability by enforcing strict type-checking and linting rules<br>- The configuration also improves build performance by utilizing module resolution suited for bundlers and excluding code generation.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/package.json'>package.json</a></b></td>
				<td>- Serves as the configuration backbone for the frontend module of the project, specifying dependencies and scripts essential for development, building, and testing<br>- It supports the React framework integration, ensuring tools like Vite, TypeScript, and ESLint are configured for efficient workflow and code quality management in the frontend development environment.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/vite.config.ts'>vite.config.ts</a></b></td>
				<td>- Defines the configuration for the Vite build tool within the frontend architecture, specifically integrating React support through plugins<br>- This setup enhances the development environment by enabling features like fast refresh and optimized build times, crucial for efficient frontend development and deployment in the project's broader ecosystem.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/index.html'>index.html</a></b></td>
				<td>- Serves as the entry point for the CV Wizard web application, establishing the foundational HTML structure and linking essential resources<br>- It sets up the viewport settings, specifies character encoding, and integrates the main TypeScript application file to activate the user interface components within the designated root element.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/eslint.config.js'>eslint.config.js</a></b></td>
				<td>- Configures ESLint for the frontend directory, focusing on TypeScript and React standards<br>- It integrates specific plugins for React hooks and refresh patterns, setting up recommended rules and ignoring compiled output<br>- The configuration ensures code adheres to best practices for a modern JavaScript and TypeScript environment, enhancing maintainability and developer productivity across the project.</td>
			</tr>
			</table>
			<details>
				<summary><b>src</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/src/main.tsx'>main.tsx</a></b></td>
						<td>- Initializes the React application by setting up the root component within a strict mode context<br>- It imports essential styles and the main application component from 'App', then mounts it to the DOM, ensuring a structured and error-checked environment for the app's frontend development.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/src/index.css'>index.css</a></b></td>
						<td>- Integrates Tailwind CSS into the frontend architecture, enabling the application of utility-first styling across the web interface<br>- By including base, components, and utilities directives, it ensures a consistent design system that enhances UI development speed and maintenance within the project's frontend framework<br>- This setup is crucial for scalable and efficient style management.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/src/App.tsx'>App.tsx</a></b></td>
						<td>- Frontend/src/App.tsx serves as the user interface for CVWizard, enabling users to upload their CVs, input job URLs, and utilize AI-driven analysis to tailor their CVs for specific job opportunities<br>- It manages user interactions, data input, and displays analysis results, integrating seamlessly with backend services for data processing and insight generation.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/src/vite-env.d.ts'>vite-env.d.ts</a></b></td>
						<td>- Frontend/src/vite-env.d.ts serves as a TypeScript declaration file that integrates Vite-specific types into the project's development environment<br>- By referencing Vite's client types, it ensures that the development tools recognize and correctly handle Vite's features, enhancing the efficiency and reliability of the frontend development process within the broader codebase architecture.</td>
					</tr>
					</table>
					<details>
						<summary><b>components</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/src/components/AnalysisResults.tsx'>AnalysisResults.tsx</a></b></td>
								<td>- AnalysisResults.tsx visualizes AI-generated insights for evaluating CV-job alignment within the frontend of the application<br>- It displays a radial chart for alignment scores, lists matched and missing keywords, and offers AI-powered suggestions to enhance CV effectiveness, contributing to a user-friendly interface that aids in optimizing job applications.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/src/components/LoadingState.tsx'>LoadingState.tsx</a></b></td>
								<td>- Provides a visual feedback component for asynchronous operations within the application's frontend<br>- It displays an animated spinner, a dynamic progress percentage, and a progress bar to indicate the status of ongoing processes, such as AI computations on user-uploaded CVs, enhancing user experience by communicating operation progress clearly.</td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>services</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/maciekmalachowski/CVWizard/blob/master/frontend/src/services/api.ts'>api.ts</a></b></td>
								<td>- Manages interactions with the backend API for a web application, facilitating the upload of CVs, retrieval of job descriptions, and generation of AI-driven insights by posting data to specific endpoints<br>- It handles data transmission securely and manages errors effectively, ensuring robust communication between the frontend and server.</td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

