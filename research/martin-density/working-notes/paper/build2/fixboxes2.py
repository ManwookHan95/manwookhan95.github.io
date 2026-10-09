d='/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/paper/newparts/'
def rep(fn,old,new):
    s=open(d+fn).read(); assert s.count(old)==1,(fn,old[:60]); s=s.replace(old,new); open(d+fn,'w').write(s)
rep('A1.tex',r"""\begin{gather*}
 \lin_b(A):=(A-a)(\zh),\qquad G_b(A):=q^*(A)-A(\zh)=q^*(A)-1-\lin_b(A),\\
 \lin_m(W_m):=\frac{\ip{W_m-w_m}{\zeta_m}}{\sigma_m},\qquad
 G_m(W_m):=N_m(W_m)-\frac{\ip{W_m}{\zeta_m}}{\sigma_m}
 =N_m(W_m)-1-\lin_m(W_m).
\end{gather*}""",r"""\begin{gather*}
 \lin_b(A):=(A-a)(\zh),\qquad G_b(A):=q^*(A)-A(\zh)=q^*(A)-1-\lin_b(A),\\
 \lin_m(W_m):=\frac{\ip{W_m-w_m}{\zeta_m}}{\sigma_m},\\
 G_m(W_m):=N_m(W_m)-\frac{\ip{W_m}{\zeta_m}}{\sigma_m}
 =N_m(W_m)-1-\lin_m(W_m).
\end{gather*}""")
rep('A3.tex',r"""\item[(E5)] the \emph{Bregman terms} $\mathrm{Bx}_m:=\ip{w'_m-w_m}{R_m\hat x'}$
satisfy $0\le\mathrm{Bx}_m\le K_es_1\sum_k\lambda_{k,m}|w'_m(k)-w_m(k)|
+2\tau(N'')$; hence""",r"""\item[(E5)] the \emph{Bregman terms} $\mathrm{Bx}_m:=\ip{w'_m-w_m}{R_m\hat x'}$
satisfy
\[
 0\le\mathrm{Bx}_m\le K_es_1\sum_k\lambda_{k,m}|w'_m(k)-w_m(k)|+2\tau(N'');
\]
hence""")
rep('A5.tex',r"""Since $q_0+\sum_m\sigma_m=1$, $\kappa_w$ is at most the max-form
coefficient $\max_\pm\max\big(h(b^\pm),\max_mH_m(\omega^\pm_m)\big)$, and it
can be much smaller.""",r"""Since $q_0+\sum_m\sigma_m=1$, the coefficient $\kappa_w$ is at most the
max-form coefficient
\[
 \kappa_{\max}:=\max_\pm\max\big(h(b^\pm),\max_mH_m(\omega^\pm_m)\big),
\]
and it can be much smaller.""")
rep('B2.tex',r"""\[
 G_m(W_m)\ge\|D_mW_m\|-\frac{\ip{D_mW_m}{D_mw_m}}{C_m}=
 \frac{\|P^\perp_mD_mW_m\|^2}{\|D_mW_m\|+\ip{D_mW_m}{D_mw_m}/C_m}\ge
 \frac{t^2}2\,\frac{H_m(\Theta_{+,m})C_m}{C_m+\eta}.
\]""",r"""\begin{align*}
 G_m(W_m)&\ge\|D_mW_m\|-\frac{\ip{D_mW_m}{D_mw_m}}{C_m}=
 \frac{\|P^\perp_mD_mW_m\|^2}{\|D_mW_m\|+\ip{D_mW_m}{D_mw_m}/C_m}\\
 &\ge\frac{t^2}2\,\frac{H_m(\Theta_{+,m})C_m}{C_m+\eta}.
\end{align*}""")
rep('B3.tex',r"""and $H_m$ vanishes on multiples of $w_m$.  As
$\sqrt{\Gamma_w}$ is a seminorm, $\sqrt{\Gamma_w(c_t)}\le\sqrt{\Gamma_w(B_+,
\Theta_+)}+\sqrt{\Gamma_w(B_+-b_t,X)}$.""",r"""and $H_m$ vanishes on multiples of $w_m$.  As $\sqrt{\Gamma_w}$ is a
seminorm,
\[
 \sqrt{\Gamma_w(c_t)}\le\sqrt{\Gamma_w(B_+,\Theta_+)}+\sqrt{\Gamma_w(B_+-
 b_t,X)}.
\]""")
rep('B3.tex',r"""$q_0h(x)\le\|U\|^2\|x\|_1^2/\nu$ and $\sigma_mH_m(X_m)\le\|D_mX_m\|_2^2/C_m\le
(\sum_k\lambda_{k,m}|X_m(k)|)^2/C_m$, and both""",r"""$q_0h(x)\le\|U\|^2\|x\|_1^2/\nu$ and
$\sigma_mH_m(X_m)\le\|D_mX_m\|_2^2/C_m\le\big(\sum_k\lambda_{k,m}|X_m(k)|
\big)^2/C_m$, and both""")
print('ok')
