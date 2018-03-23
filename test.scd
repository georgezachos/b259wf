{ FaustB259wf.ar( SinOsc.ar(440, 0, MouseX.kr(0.1, 10, 1)), SinOsc.ar(440, 0, MouseX.kr(0.1, 10, 1)) )}.play;


{ Fold.ar(SinOsc.ar(440, 0, MouseX.kr(-10, -0.1, 1)), MouseX.kr(-0.1, -10, 1), MouseX.kr(0.1, 10, 1)) }.play;
(
b = Buffer.read(s, "/Users/qfwfq/Music/Second Woman - Second Woman (spectrum spools, 2016) (flac)/08 800438ul8.flac"); // remember to free the buffer later.
SynthDef(\help_PlayBuf, {| out = 0, bufnum = 0 |
    Out.ar(out,
		        FaustB259wf.ar(MouseX.kr(1,10,1)*PlayBuf.ar(2, bufnum, BufRateScale.kr(bufnum), doneAction: Done.freeSelf))
		// Fold.ar( PlayBuf.ar(2, bufnum, BufRateScale.kr(bufnum), doneAction: Done.freeSelf)*MouseX.kr(-10, -0.1, 1), MouseX.kr(-0.1, -10, 1), MouseX.kr(0.1, 10, 1))
    )
}).play(s, [\out, 0, \bufnum, b]);
)