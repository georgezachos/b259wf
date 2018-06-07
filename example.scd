(
{
	~f=thisProcess.nowExecutingPath.dirname++"/test.wav";
	b = Buffer.read(s, ~f);
	FaustB259wf.ar( PlayBuf.ar(1, b, BufRateScale.kr(b), loop:1)!2, fold:MouseX.kr(0,1), lowpass:MouseX.kr(1,0), offset:MouseY.kr(0,1))
}.scope;
)

(
{
	FaustB259wf.ar( DPW3Tri.ar(100,mul:0.9)!2, fold:MouseX.kr(0,1), lowpass:MouseX.kr(1,0), offset:MouseY.kr(0,1))
}.scope;
)
