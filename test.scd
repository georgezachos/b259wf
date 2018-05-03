s.options.device = "Built-in Output";
{ FaustB259wf.ar( SinOsc.ar(490, 0, MouseX.kr(0.1, 10, 1)), SinOsc.ar(440, 0, MouseX.kr(0.1, 10, 1)) )}.plot(0.005);
{ FaustB259wfBlamp2.ar( SinOsc.ar(490, 0, MouseX.kr(0.1, 10, 1)), SinOsc.ar(440, 0, MouseX.kr(0.1, 10, 1)) )}.plot(0.005);
{ FaustB259wfBlamp2.ar( SinOsc.ar(910, 0, MouseX.kr(0.1, 10, 1)), SinOsc.ar(440, 0, MouseX.kr(0.1, 10, 1)) )}.plot(0.002);
{ FaustB259wf.ar( SinOsc.ar(910, 0, MouseX.kr(0.1, 10, 1)), SinOsc.ar(440, 0, MouseX.kr(0.1, 10, 1)) )}.plot(0.002);

o = ServerOptions.new();
o.hardwareBufferSize = 1024
o.blockSize = 256
o.blockSize
{FaustB259wf.ar( SinOsc.ar(700), (SinOsc.ar(12)+1)/2, SinOsc.ar(10))}.scope;
{b = Buffer.read(s, ~f); FaustB259wf.ar( PlayBuf.ar(2, b, BufRateScale.kr(b)), (SinOsc.ar(0.3)+1)/2, 0)}.scope;
{b = Buffer.read(s, ~f); FaustB259wf.ar( PlayBuf.ar(2, b, BufRateScale.kr(b)), k.elAt(\kn, 0, 0).action_({|el| el.value}), k.elAt(\kn, 1, 1).value, k.elAt(\kn, 1, 2).value)}.scope;
k.elAt(\kn, 1, 0).value
{SawDPW.ar(540)}.scope
~f = "/Users/nan/Music/AFX & Luke Vibert - Orphans EP (2017)/04 - AFX - 4x Atlantis take1.flac"
~f = "/Users/nan/Music/AFX & Luke Vibert - Orphans EP (2017)/02 - Luke Vibert - spiral staircase [future music competition] [AFX ALTremix b] .flac"
~f = "/Users/nan/Music/pole - 1 2 3 [sc 054cd]/3 04 uberfahrt.mp3"
~f = "/Users/nan/Downloads/39432__erh__bluebeat-01.wav"
"/Users/gz/Downloads/191735__keinzweiter__acid-loop-120.aiff"
"/Users/gz/Downloads/339563__nototo84__acid-riff-synth.wav"
"/Users/gz/Downloads/340488__djfroyd__frequency-modulated-bass.wav"
"/Users/gz/Downloads/414352__gis-sweden__electronic-minute-no-30-8-tones-and-tempo-change.wav"
"/Users/gz/Downloads/214335__timmyozone__rugrats-synth-sounds.wav"
~f = "/Users/nan/Downloads/19377__notofficial__3034myg.wav"
~f = "/Users/nan/Downloads/27130__pryght-one__harp.wav"
{ Fold.ar(SinOsc.ar(440, 0, MouseX.kr(-10, -0.1, 1)), MouseX.kr(-0.1, -10, 1), MouseX.kr(0.1, 10, 1)) }.play;

(
b = Buffer.read(s, ~f); // remember to free the buffer later.
SynthDef(\wfolder, {| out = 0, bufnum = 0, gain=0, lp=1, offset=0 |
	// Out.ar(out, FaustB259wf.ar(PlayBuf.ar(2, bufnum, BufRateScale.kr(bufnum), doneAction: Done.freeSelf), gain, lp, offset)
	Out.ar(out, FaustB259wf.ar(In.ar(2,1), gain, lp, offset))
}).add;
k = MKtl('mft', "midi-fighter-twister");
// k.gui;
k.elAt(\kn, 0, 0).action_({|el|  a.set(\gain, el.value)});
k.elAt(\kn, 0, 1).action_({|el|  a.set(\lp, el.value)});
k.elAt(\kn, 0, 2).action_({|el|  a.set(\offset, el.value)});
)

a = Synth(\wfolder, [\out, 0, \bufnum, b])


a.set(\gain, 0)
(
{FaustB259wf.ar(MouseX.kr(1,10,1)*PlayBuf.ar(2, b, BufRateScale.kr(b), doneAction: Done.freeSelf))}.plot(5)
)

{SinOsc.ar(400+SinOsc.ar(100,0,200))}.plot(0.025)

(
w = Window("BLAMP", Rect(0, 0, 511, 300)); // width should be 511
f = FreqScopeView(w, w.view.bounds);
f.active_(true); // turn it on the first time;

w.onClose_({ f.kill }); // you must have this
w.front;
// { FaustB259wfBlamp2.ar( SinOsc.ar(MouseY.kr(30, 2000, 1), 0, MouseX.kr(0.1, 10, 1)) )}.play(s); // start two sine waves
f.dbRange_(100); // expand amplitude range
)

(
w = Window("-", Rect(0, 0, 511, 300)); // width should be 511
f = FreqScopeView(w, w.view.bounds);
f.active_(true); // turn it on the first time;

w.onClose_({ f.kill }); // you must have this
w.front;
{ FaustB259wf.ar( SinOsc.ar(MouseY.kr(30, 2000, 1), 0, MouseX.kr(0.1, 10, 1)) )}.play(s); // start two sine waves
f.dbRange_(100); // expand amplitude range

)
f.freqMode_(1); // change to log scale so we can see them
f.inBus_(1); // look at bus 1
f.dbRange_(100); // expand amplitude range
f.active_(false); // turn scope off (watch CPU)
f.active_(true); // turn it back on
f.bufSize
{ Mix.ar(SinOsc.ar([500, 1200, 3000, 9000, 12000], 0, [0.2, 0.1, 0.05, 0.03, 0.01])) }.play(s); // restart some sines
