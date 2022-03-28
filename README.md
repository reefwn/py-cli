# Python Command-Line Interface

## Copy file to bin folder

```
cp {filename}.py bin/{filename}
```

## Make the file in the bin folder executable

```
chmod +x bin/{filename}
```

## Copy config file to bin folder

```
cp config/{filename} bin/config/{filename}
```

### Add PATH to shell profile (bash / zsh)

```
export PATH=$PATH":$HOME/{path_to_this_repo}/bin"
```

### Update shell profile with added PATH

```
source ~/.{shell_profile}
```

## Technologies & IDE

<div>
    <img style="float: left" src="https://code.visualstudio.com/assets/updates/1_35/logo-stable.png" height="48" alt="vscode">
</div>
