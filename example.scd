(
{
	~f="/Users/george/Downloads/404812__acpsy__sawbass.wav";
	b = Buffer.read(s, ~f);
	f=1;
	FaustB259wf.ar( PlayBuf.ar(1, b, BufRateScale.kr(b), loop:1), fold:MouseX.kr(0,1), lowpass:MouseX.kr(1,0), offset:MouseY.kr(0,1))
}.scope;
)