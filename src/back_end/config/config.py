from pydantic import BaseModel
from typing import Optional


class Requirements(BaseModel):
    age_range: str
    work_arrangement: str
    education_level: str
    role: str
    years_of_experience: int
    programming_languages: Optional[str] = None
    databases: Optional[str] = None
    cloud_platforms: Optional[str] = None
    web_frameworks: Optional[str] = None
    other_frameworks: Optional[str] = None
    developer_tools: Optional[str] = None
    development_environments: Optional[str] = None
    operating_systems: Optional[str] = None
    collaboration_tools: Optional[str] = None
    communication_tools: Optional[str] = None


BINARY_RELEVANCE_ENCODED_VALUES = {
    "LanguageHaveWorkedWith": ["Ada", "Apex", "APL", "Assembly", "Bash/Shell (all shells)", "C", "C#", "C++", "Clojure", "Cobol", "Crystal", "Dart", "Delphi", "Elixir", "Erlang", "F#",
                               "Flow", "Fortran", "GDScript", "Go", "Groovy", "Haskell", "HTML/CSS", "Java", "JavaScript", "Julia", "Kotlin", "Lisp", "Lua", "MATLAB", "Nim", "Objective-C",
                               "OCaml", "Perl", "PHP", "PowerShell", "Prolog", "Python", "R", "Raku", "Ruby", "Rust", "SAS", "Scala", "Solidity", "SQL", "Swift", "TypeScript", "VBA",
                               "Visual Basic (.Net)", "Zig"],
    "DatabaseHaveWorkedWith": ["BigQuery", "Cassandra", "Clickhouse", "Cloud Firestore", "Cockroachdb", "Cosmos DB", "Couch DB", "Couchbase", "Datomic", "DuckDB", "Dynamodb",
                               "Elasticsearch", "Firebase Realtime Database", "Firebird", "H2", "IBM DB2", "InfluxDB", "MariaDB", "Microsoft Access", "Microsoft SQL Server", "MongoDB",
                               "MySQL", "Neo4J", "Oracle", "PostgreSQL", "RavenDB", "Redis", "Snowflake", "Solr", "SQLite", "Supabase", "TiDB"],
    "PlatformHaveWorkedWith": ["Amazon Web Services (AWS)", "Cloudflare", "Colocation", "Digital Ocean", "Firebase", "Fly.io", "Google Cloud", "Heroku", "Hetzner", "IBM Cloud Or Watson",
                               "Linode", "Managed Hosting", "Microsoft Azure", "Netlify", "OpenShift", "OpenStack", "Oracle Cloud Infrastructure (OCI)", "OVH", "Render", "Scaleway",
                               "Vercel", "VMware", "Vultr"],
    "WebframeHaveWorkedWith": ["Angular", "AngularJS", "ASP.NET", "ASP.NET CORE", "Blazor", "CodeIgniter", "Deno", "Django", "Drupal", "Elm", "Express", "FastAPI", "Fastify", "Flask",
                               "Gatsby", "jQuery", "Laravel", "Lit", "NestJS", "Next.js", "Node.js", "Nuxt.js", "Phoenix", "Play Framework", "Qwik", "React", "Remix", "Ruby on Rails",
                               "Solid.js", "Spring Boot", "Svelte", "Symfony", "Vue.js", "WordPress"],
    "MiscTechHaveWorkedWith": [".NET (5+)", ".NET Framework (1.0 - 4.8)", ".NET MAUI", "Apache Kafka", "Apache Spark", "Capacitor", "Cordova", "CUDA", "Electron", "Flutter", "GTK", "Hadoop",
                               "Hugging Face Transformers", "Ionic", "JAX", "Keras", "Ktor", "MFC", "Micronaut", "NumPy", "Opencv", "OpenGL", "Pandas", "Qt", "Quarkus", "RabbitMQ",
                               "React Native", "Scikit-Learn", "Spring Framework", "SwiftUI", "Tauri", "TensorFlow", "Tidyverse", "Torch/PyTorch", "Uno Platform", "Xamarin"],
    "ToolsTechHaveWorkedWith": ["Ansible", "Ant", "APT", "bandit", "Boost.Test", "build2", "Bun", "Cargo", "Catch2", "Chef", "Chocolatey", "CMake", "Composer", "cppunit", "CUTE", "Dagger",
                                "Docker", "doctest", "ELFspy", "GNU GCC", "Godot", "Google Test", "Gradle", "Homebrew", "Kubernetes", "lest", "liblittletest", "LLVM's Clang", "Make",
                                "Maven (build tool)", "Meson", "MSBuild", "MSVC", "Ninja", "Nix", "npm", "NuGet", "Pacman", "Pip", "pnpm", "Podman", "Pulumi", "Puppet", "QMake", "SCons",
                                "snitch", "Terraform", "tunit", "Unity 3D", "Unreal Engine", "Visual Studio Solution", "Vite", "Wasmer", "Webpack", "Yarn"],
    "NEWCollabToolsHaveWorkedWith": ["Android Studio", "Atom", "BBEdit", "CLion", "Code::Blocks", "condo", "DataGrip", "Eclipse", "Emacs", "Fleet", "Geany", "Goland", "Helix",
                                     "IntelliJ IDEA", "IPython", "Jupyter Notebook/JupyterLab", "Kate", "Micro", "Nano", "Neovim", "Netbeans", "Notepad++", "Nova", "PhpStorm", "PyCharm",
                                     "Qt Creator", "Rad Studio (Delphi, C++ Builder)", "Rider", "RStudio", "RubyMine", "Spyder", "Sublime Text", "TextMate", "Vim", "Visual Studio",
                                     "Visual Studio Code", "VSCodium", "WebStorm", "Xcode"],
    "OpSysPersonal use": ["AIX", "Android", "Arch", "BSD", "ChromeOS", "Cygwin", "Debian", "Fedora", "Haiku", "iOS", "iPadOS", "MacOS", "Other Linux-based", "Red Hat", "Solaris", "Ubuntu",
                          "Windows", "Windows Subsystem for Linux (WSL)"],
    "OfficeStackAsyncHaveWorkedWith": ["Adobe Workfront", "Airtable", "Asana", "Azure Devops", "Basecamp", "Cerri", "Clickup", "Confluence", "Dingtalk (Teambition)", "Document360",
                                       "Doxygen", "GitHub Discussions", "Jira", "Leankor", "Linear", "Markdown File", "Microsoft Lists", "Microsoft Planner", "Miro", "Monday.com", "Notion",
                                       "Nuclino", "Planview Projectplace Or Clarizen", "Redmine", "Redocly", "Shortcut", "Smartsheet", "Stack Overflow for Teams", "Swit", "Tettra", "Trello",
                                       "Wikis", "Wimi", "Workzone", "Wrike", "YouTrack"],
    "OfficeStackSyncHaveWorkedWith": ["Cisco Webex Teams", "Coolfire Core", "Discord", "Google Chat", "Google Meet", "IRC", "Jitsi", "Matrix", "Mattermost", "Microsoft Teams", "Ringcentral",
                                      "Rocketchat", "Signal", "Skype", "Slack", "Symphony", "Telegram", "Unify Circuit", "Whatsapp", "Wickr", "Wire", "Zoom", "Zulip"]
}

COLUMN_NEW_ORDER = ["Age", "RemoteWork", "EdLevel", "YearsCode", "DevType", "LanguageHaveWorkedWith", "DatabaseHaveWorkedWith", "PlatformHaveWorkedWith", "WebframeHaveWorkedWith",
                    "MiscTechHaveWorkedWith", "ToolsTechHaveWorkedWith", "NEWCollabToolsHaveWorkedWith", "OpSysPersonal use", "OfficeStackAsyncHaveWorkedWith",
                    "OfficeStackSyncHaveWorkedWith"]

COLUMN_RENAME_DICT = {
    "age_range": "Age",
    "work_arrangement": "RemoteWork",
    "education_level": "EdLevel",
    "role": "DevType",
    "years_of_experience": "YearsCode",
    "programming_languages": "LanguageHaveWorkedWith",
    "databases": "DatabaseHaveWorkedWith",
    "cloud_platforms": "PlatformHaveWorkedWith",
    "web_frameworks": "WebframeHaveWorkedWith",
    "other_frameworks": "MiscTechHaveWorkedWith",
    "developer_tools": "ToolsTechHaveWorkedWith",
    "development_environments": "NEWCollabToolsHaveWorkedWith",
    "operating_systems": "OpSysPersonal use",
    "collaboration_tools": "OfficeStackAsyncHaveWorkedWith",
    "communication_tools": "OfficeStackSyncHaveWorkedWith"
}


ONE_HOT_ENCODED_VALUES = {
    "Age": ["18-24 years old", "25-34 years old", "35-44 years old", "45-54 years old", "55-64 years old", "65 years or older", "Prefer not to say", "Under 18 years old"],
    "RemoteWork": ["Hybrid (some remote, some in-person)", "In-person", "Null", "Remote"],
    "EdLevel": ["Associate degree (A.A., A.S., etc.)", "Bachelor's degree (B.A., B.S., B.Eng., etc.)", "Master's degree (M.A., M.S., M.Eng., MBA, etc.)", "Primary/elementary school",
                "Professional degree (JD, MD, Ph.D, Ed.D, etc.)", "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)",
                "Some college/university study without earning a degree", "Something else"],
    "DevType": ["Academic researcher", "Blockchain", "Cloud infrastructure engineer", "Data or business analyst", "Data scientist or machine learning specialist", "Database administrator",
                "Designer", "DevOps specialist", "Developer Advocate", "Developer Experience", "Developer, QA or test", "Developer, back-end",
                "Developer, desktop or enterprise applications", "Developer, embedded applications or devices", "Developer, front-end", "Developer, full-stack",
                "Developer, game or graphics", "Developer, mobile", "Educator", "Engineer, data", "Engineer, site reliability", "Engineering manager", "Hardware Engineer",
                "Marketing or sales professional", "Null", "Product manager", "Project manager", "Research & Development role", "Scientist", "Security professional",
                "Senior Executive (C-Suite, VP, etc.)", "Student", "System administrator"]
}
