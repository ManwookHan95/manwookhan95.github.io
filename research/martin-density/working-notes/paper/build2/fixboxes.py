import os
d='/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/paper/newparts/'
def rep(fn,old,new):
    s=open(d+fn).read(); assert s.count(old)==1,(fn,old[:60]); s=s.replace(old,new); open(d+fn,'w').write(s)
rep('A1.tex',r"""\[
 E:=\sum_m|\varepsilon_m|\iota_m+|\lambda|\big(|q^*(A)-1|+q^*(A-a)\big)
 +\max_m\frac{4|\varepsilon_m|\,\|D_m(W_m-w_m)\|_2\|D_my_m\|_2
 +\varepsilon_m^2\|D_my_m\|_2^2}{C_m}.
\]""",r"""\begin{multline*}
 E:=\sum_m|\varepsilon_m|\iota_m+|\lambda|\big(|q^*(A)-1|+q^*(A-a)\big)\\
 +\max_m\frac{4|\varepsilon_m|\,\|D_m(W_m-w_m)\|_2\|D_my_m\|_2
 +\varepsilon_m^2\|D_my_m\|_2^2}{C_m}.
\end{multline*}""")
rep('A2.tex',r"""\[
 \Psi(y):=\sup\Big\{2g(Uk+\chi_c)-\frac\nu{q_0}\|k\|^2:\ k\perp e,\ \chi_c\in
 C_+,\ \mathfrak d(Uk+\chi_c)=y\Big\}\qquad(\sup\emptyset=-\infty).
\]""",r"""\[
 \Psi(y):=\sup\Big\{2g(Uk+\chi_c)-\frac\nu{q_0}\|k\|^2:\ k\perp e,\ \chi_c\in
 C_+,\ \mathfrak d(Uk+\chi_c)=y\Big\}
\]
($\sup\emptyset:=-\infty$).""")
rep('A3.tex',r"""\begin{gather*}
 a'':=a+\sum_{j\in K\cap[1,N]}m_jz_je_j^*,\qquad a':=a''/q^*(a''),\qquad
 e':=U^*a'/\|U^*a'\|,\\
 z'_j:=z_j\ (j\le N''),\quad z'_j:=0\ (j>N''),\qquad \hat x':=z'+Ue',\qquad
 x':=\hat x'/p(\hat x'),\qquad f':=\nabla p(x').
\end{gather*}""",r"""\begin{gather*}
 a'':=a+\sum_{j\in K\cap[1,N]}m_jz_je_j^*,\qquad a':=a''/q^*(a''),\qquad
 e':=U^*a'/\|U^*a'\|,\\
 z'_j:=z_j\ (j\le N''),\qquad z'_j:=0\ (j>N''),\qquad \hat x':=z'+Ue',\\
 x':=\hat x'/p(\hat x'),\qquad f':=\nabla p(x').
\end{gather*}""")
rep('A3.tex',r"""\item[(E4)] for every $\omega\in c_{00}$ vanishing on $P_m\cup P'_m$,
$|d'_m(\omega)-d_m(\omega)|\le K(\omega)(s_1+\tau(N''))$, where
$d'_m(\omega):=\ip{D_mw'_m}{D_m\omega}/C'_m$ and $K(\omega)$ depends only on
$f,g,\rho,\omega$;""",r"""\item[(E4)] for every $\omega\in c_{00}$ vanishing on $P_m\cup P'_m$ we
have $|d'_m(\omega)-d_m(\omega)|\le K(\omega)(s_1+\tau(N''))$, where
$d'_m(\omega):=\ip{D_mw'_m}{D_m\omega}/C'_m$ and the constant $K(\omega)$
depends only on $f,g,\rho,\omega$;""")
rep('A3.tex',r"""\[
 \|D(w'-w)\|_2^2\le\sum_k\min(K_Fs_1,2\Phi_k)^2+4K_F\sum_k\Phi_kt_k
 \le K_F^2s_1^2\lceil\log_2(1/s_1)\rceil+\tfrac43s_1^2+4K_Fs_1^2 .
 \qedhere
\]""",r"""\begin{align*}
 \|D(w'-w)\|_2^2&\le\sum_k\min(K_Fs_1,2\Phi_k)^2+4K_F\sum_k\Phi_kt_k\\
 &\le K_F^2s_1^2\lceil\log_2(1/s_1)\rceil+\tfrac43s_1^2+4K_Fs_1^2 .
 \qedhere
\end{align*}""")
rep('A3.tex',r"""\[
 \|Dy\|^2=C'^2+2\ip{Dw'}{DY}+\|DY\|^2=2C'^2-C^2+\mathcal X_0,\qquad
 \mathcal X_0:=\|D(w'-w)\|^2+\|DY\|^2-2R_A .
\]""",r"""\begin{gather*}
 \|Dy\|^2=C'^2+2\ip{Dw'}{DY}+\|DY\|^2=2C'^2-C^2+\mathcal X_0,\\
 \mathcal X_0:=\|D(w'-w)\|^2+\|DY\|^2-2R_A .
\end{gather*}""")
rep('A3.tex',r"""\[
 \mathfrak S_m:=\|D_m(w'_m-w_m)\|_2^2+\sum_{k\in A_m}\Big(\Phi_m(k)^2+
 \lambda_{k,m}\big(|w'_m(k)-w_m(k)|+(C'_m-C_m)_+\big)\Big)=o(s_1).
\]""",r"""\begin{multline*}
 \mathfrak S_m:=\|D_m(w'_m-w_m)\|_2^2\\
 +\sum_{k\in A_m}\Big(\Phi_m(k)^2+
 \lambda_{k,m}\big(|w'_m(k)-w_m(k)|+(C'_m-C_m)_+\big)\Big)=o(s_1).
\end{multline*}""")
rep('A5.tex',r"""Since $q_0+\sum_m\sigma_m=1$, $\kappa_w$ is at most the max-form coefficient
$\max_\pm\max(h(b^\pm),\max_mH_m(\omega^\pm_m))$, and it can be much
smaller.""",r"""Since $q_0+\sum_m\sigma_m=1$, $\kappa_w$ is at most the max-form
coefficient $\max_\pm\max\big(h(b^\pm),\max_mH_m(\omega^\pm_m)\big)$, and it
can be much smaller.""")
rep('B2.tex',r"""Lemma~\ref{lem:bookkeeping}(c), $G_m(W_m)\ge\|D_mW_m\|-\ip{D_mW_m}{D_mw_m}
/C_m=\|P^\perp_mD_mW_m\|^2/(\|D_mW_m\|+\ip{D_mW_m}{D_mw_m}/C_m)\ge
\frac{t^2}2H_m(\Theta_{+,m})C_m/(C_m+\eta)$, by Lemma~\ref{lem:smallness}.""",
r"""Lemma~\ref{lem:bookkeeping}(c) and Lemma~\ref{lem:smallness},
\[
 G_m(W_m)\ge\|D_mW_m\|-\frac{\ip{D_mW_m}{D_mw_m}}{C_m}=
 \frac{\|P^\perp_mD_mW_m\|^2}{\|D_mW_m\|+\ip{D_mW_m}{D_mw_m}/C_m}\ge
 \frac{t^2}2\,\frac{H_m(\Theta_{+,m})C_m}{C_m+\eta}.
\]""")
rep('B3.tex',r"""For $t\in\mathcal W(l_*)$ let $\kappa_t:=(B_+1_F)(\zh)$,
$b_t:=B_+1_F-\kappa_ta$, and in block $m$ let
$\omega^c_m(k):=\max\{-2\gap_m(k)/t,\min\{\omega_{+,m}(k),2\gap_m(k)/t\}\}$
if $k\in Q_m$, $\iota(k,m)\le l_*$ and $\gap_m(k)\ge t^2$, and
$\omega^c_m(k):=0$ otherwise.  Put $c_t:=(b_t,(\omega^c_m)_m)$.""",
r"""For $t\in\mathcal W(l_*)$ let $\kappa_t:=(B_+1_F)(\zh)$,
$b_t:=B_+1_F-\kappa_ta$, and in block $m$ let
\[
 \omega^c_m(k):=\max\Big\{-\frac{2\gap_m(k)}t,\min\Big\{\omega_{+,m}(k),
 \frac{2\gap_m(k)}t\Big\}\Big\}
\]
if $k\in Q_m$, $\iota(k,m)\le l_*$ and $\gap_m(k)\ge t^2$, and
$\omega^c_m(k):=0$ otherwise.  Put $c_t:=(b_t,(\omega^c_m)_m)$.""")
rep('B3.tex',r"""\[
 \sum_k\Phi_k|\omega_+(k)-\omega^c(k)|\le\frac1m\sum_{\rm coarse}
 \lambda_k\rho_k+\sum_{\rm fine}\Phi_k(|\Theta_+(k)|+|d_+|M)\le
 \frac1m\sum_{\rm coarse}\lambda_k\rho_k+3t^2+\Big(\frac3t+\frac
 t\sigma\Big)t^3,
\]""",r"""\begin{align*}
 \sum_k\Phi_k|\omega_+(k)-\omega^c(k)|&\le\frac1m\sum_{\rm coarse}
 \lambda_k\rho_k+\sum_{\rm fine}\Phi_k(|\Theta_+(k)|+|d_+|M)\\
 &\le\frac1m\sum_{\rm coarse}\lambda_k\rho_k+3t^2+\Big(\frac3t+\frac
 t\sigma\Big)t^3,
\end{align*}""")
rep('B3.tex',r"""(d) The pair of $c_t$ is $(b_t,(\omega^c_m-d_m(\omega^c_m)w_m))=(B_+,\Theta_+)
-(B_+-b_t,(X_m))$, and $H_m$ vanishes on multiples of $w_m$.""",
r"""(d) The pair of $c_t$ is
\[
 \big(b_t,(\omega^c_m-d_m(\omega^c_m)w_m)_m\big)=(B_+,\Theta_+)-\big(B_+-b_t,
 (X_m)_m\big),
\]
and $H_m$ vanishes on multiples of $w_m$.""")
print('done')
