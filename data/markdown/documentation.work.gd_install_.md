
# Install VectorForgeML - Setup Guide for R & C++ ML Framework

URL: https://documentation.work.gd/install/

Install VectorForgeML
VectorForgeML is available on CRAN and installs directly via install.packages()
.
Step 1: Prerequisites
Ensure you have R (≥ 4.0.0) and a C++ compiler installed on your system.
- Windows: Install RTools
- macOS: Install Xcode Command Line Tools (
xcode-select --install
) - Linux: Install
build-essential
andr-base-dev
Step 2: Install from CRAN (Recommended)
VectorForgeML is published on CRAN and can be installed with a single command.
install.packages("VectorForgeML")
library(VectorForgeML)
Step 3: Verify Installation
library(VectorForgeML)
# Check available functions
ls("package:VectorForgeML")
You should see 30+ functions listed. Ready to go! Check out the documentation for quick start guides.
Development Version (GitHub)
To install the latest development version with the newest features and fixes, use the remotes
package.
install.packages("remotes", repos="https://cloud.r-project.org")
remotes::install_github("mohd-musheer/VectorForgeML")
Note: The development version may contain experimental features. For production use, the CRAN release is recommended.
Troubleshooting
Compiler Errors on Windows
If you encounter compilation errors on Windows, ensure RTools is installed and added to your
PATH. Verify with Sys.which("make")
in R.
macOS Compilation Issues
On macOS, ensure Xcode Command Line Tools are installed: xcode-select --install
. For M1/M2 Macs, ensure you have the ARM-compatible R version.
