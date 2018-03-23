import("stdfaust.lib");
import("basics.lib");
import("maths.lib");

R1 = (10., 49.9, 91., 30., 68.);
r2 = 100.;
R3 = (100., 43.2, 56., 68., 33., 240.);
C = (0.-12., 0.-27.777, .0-21.428, 17.647, 36.363);
Vs = 6.;

r1(k) = ba.take(k+1, R1);
r3(k) = ba.take(k+1, R3);
c(k) = ba.take(k+1, C);

term1(k) = Vs*r1(k)/r2;

invClipCond(sig, k) = ma.fabs(sig) > term1(k);
invClipNo(sig, k) = ma.signum(sig) * term1(k);
invClip(sig, k) = ba.if(invClipCond(sig, k), sig, invClipNo(sig, k));

term2(k) = (r2*r3(k)/(r1(k)*r3(k) + r2*r3(k) + r1(k)*r2));
term3(clipped, k) = (clipped - ma.signum(clipped)*term1(k))* c(k);

revClip(sig, k) = term2(k) * term3(sig, k);

folderBranches(sig) = sig <: par(i, 5, revClip(invClip(sig,i), i)); 
/*folderBranches(sig) = sig <: par(i, 5, invClip(sig,i));*/
wf(sig) = sig <: ( (folderBranches(sig) :> _) + (5.*sig) ) / 15.;

/* process = invClip(_, 4); */
process = wf(_);
