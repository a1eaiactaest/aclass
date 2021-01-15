# aclass

Tool making your quarantine life so much easier.

Are you tired of typing in credentials of your online classes?
I came up with solution. Now you can install aclass python package with `pip3`.

### Installation

```bash
pip3 install aclass
```

### Configuration

To configure aclass after installation run:

```bash
aclass --configure
```

This command will create ```classes.json``` file in root directory of package.
After json file is create you will be redirected to [vim](https://www.vim.org/) in order to edit the already created template.
Template is located [here](docs/classes.json).

**Running this command again will overwrite already existing file and remove all contents.**

### Example

```json
{
  "maths": "link to your maths class",
  "cs": "link to your cs class"
}
```

If you are wondering how json syntax works visit [this page](https://javaee.github.io/tutorial/jsonp001.html).

### Usage

Joining to your class is pretty simple. As the second argument you take name of object you assigned link in ```classes.json``` to.
For example; in example above we have two classes: "maths" and "cs". You can name however you want. Key is to remember name of object.

If you would like to join to your Computer Science class:

```bash
aclass --join name-of-cs-class-in-json-file
```
