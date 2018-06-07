# b259wf

This is a model of the "tibre" circuit of the Buchla 259 Complex Wave Generator,
made in [Faust](http://faust.grame.fr/). The model follows the circuit modelling
as seen on the paper  [Virtual Analog Buchkla 259
wavefolder](http://www.dafx17.eca.ed.ac.uk/papers/DAFx17_paper_82.pdf), using 5 folds. The proposed 2-point BLAMP
antialiasing method has been attempted for arbitrary sources as shown
[here](http://dafx16.vutbr.cz/dafxpapers/18-DAFx-16_paper_33-PN.pdf), but it is
not sufficient for high frequencies and/or more complex signals. Instead, filtering and
light cubic nonlinearity distiorion has been used to round corners and for
clipping. The user interface consists of the controls **fold** for the folding
amount, **offset** for offseting the signal before folding, and **lowpass**
as a final stage one-pole filtering to control the character (too much folding
might introduce unwanted higher harmonics for certain signals). The final output
is dc-blocked.

## Instructions 

Clone the repository:

`git clone https://github.com/georgezachos/b259wf`

This includes the UGen binary for using with supercollider (the `*.sc` and
`*.scx` files). Note this is compiled and tested only under OSX. 
Copy the relevant files to the SC extension folder:

```
cd b259wf
cp {b259wf.sc,b259wf.scx} <path/to/SC/extensions>
```
From SuperCollider run:

`Platform.userExtensionDir` to find the user folder, or

`Platform.systemExtensionDir` for the system one

The file `test.scd` includes an example using the provided sample with SuperCollider.

### Manual compilation

The easiest way to compile binaries from the `.dsp` file, is by using the [Faust online
compiler](https://faust.grame.fr/onlinecompiler/). If you are compiling for SuperCollider though, the online compiler exports will
be unusable for versions >=3.9. You should instead compile it locally, on your
machine. 

You should have the latest Faust instaled, and have access to the
`faust2<export mode>` binaries. The SC headers are needed for
`faust2supercollider`. Assuming you are on your user directory:

```
git clone https://github.com/supercollider/supercollider.git
export SUPERCOLLIDER_HEADERS=/path/to/supercollider/include
faust2supercollider path/to/b259wf/b259wf.dsp
```
