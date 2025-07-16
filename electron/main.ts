import { app, BrowserWindow } from 'electron';
import * as path from 'path';
import { spawn, ChildProcess } from 'child_process';
const isDev = process.env.NODE_ENV === 'development';

let backendProc: ChildProcess;

function startBackend() {
  const backendDir = path.resolve(__dirname, '../backend');
  console.log("Launching Python from", backendDir);
  backendProc = spawn('python3', ['api.py', ''], {
    cwd: backendDir,
    stdio: 'inherit',
  });
}
function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
    },
  });

  if (isDev) {
    win.loadURL('http://localhost:8080');
    win.webContents.openDevTools();
  } else {
    win.loadFile(path.join(__dirname, '../dist/index.html'));
  }
}

app
  .whenReady()
  .then(() => {
    startBackend();
    createWindow();
  })

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
