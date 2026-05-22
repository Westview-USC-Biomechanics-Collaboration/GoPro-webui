# Go Pro Web UI
![Screenshot of UI](docs/media/image.png)
## Usage
First clone the repository.
```bash
git clone ""
```
### Depedencies
First you need nodejs and npm
```bash
# Restart terminal after running
winget install -e --id OpenJS.NodeJS

# Should return version of node and npm
node -v
npm -v
```
### Backend
Enter the backend Directory
```bash
cd ./backend
```
Now, create a venv and activate it
```
python -m venv .venv

./.venv/Scripts/Activate
```
Install the dependencies:
```bash
pip install -r requirements.txt
```
Run the app.
```
python main.py
```
### Front End
CD to the root directory of the project and then run
```bash
# Build Project
npm run build

PORT=80 node build
```
## Development

## Wiki