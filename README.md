# Keyboard Customization (Mac & Linux)

This project version controls keyboard configurations for both macOS (Karabiner) and Linux (Kanata).

## Mac (Karabiner-Elements)

This is a personal project to version control and automate the configuration file of [Karabiner Elements](https://karabiner-elements.pqrs.org/), a powerful and stable keyboard customizer for MacOs.

The project arose from the painstaking process of adding new rules to karabiner using the UserUX, which does not keep track of changes as well as provide no formatting for json files.

By separating each rule in a single file and being able to edit it in vscode, changes are much easier to make but also version controlled using git.

## Linux (Kanata)
The Linux configuration is located at `kanata.kbd` in this repository. It is **symlinked** to `~/.config/kanata/kanata.kbd`.

### How to Update (Linux)
1. **Modify**: Open and edit `kanata.kbd` directly in this repository.
2. **Apply**: Restart the Kanata service to load your changes:
   ```bash
   systemctl --user restart kanata.service
   ```
3. **Verify**: Check if the service is running properly:
   ```bash
   systemctl --user status kanata.service
   ```
4. **Version Control**: Save your change to Git:
   ```bash
   git add kanata.kbd
   git commit -m "Update keyboard layout"
   ```

> [!TIP]
> You can check if your configuration is valid before applying it by running:
> `/usr/local/bin/kanata --cfg kanata.kbd --check`

### Known issues with karabiner
- [ ] Left Command (acting as control) + key does not work in antigravity;
- [ ] Function key not used;
- [ ] Tab is acting as switching focus on antigravity - working fine on everything else;
- [ ] Focus on agent view - probably unrelated to kanata;