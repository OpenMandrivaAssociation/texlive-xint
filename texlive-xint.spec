# revision 32271
# category Package
# catalog-ctan /macros/generic/xint
# catalog-date 2013-11-28 18:24:01 +0100
# catalog-license lppl1.3
# catalog-version 1.09h
Name:		texlive-xint
Version:	1.09h
Release:	3
Summary:	Expandable operations on long numbers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/xint
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xint.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xint.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xint.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides four packages: - xint, which provides
expandable TeX macros that implement the basic arithmetic
operations of addition, subtraction, multiplication and
division, as applied to arbitrarily long numbers represented as
chains of digits with an optional minus sign; - xintgcd, which
provides implementations of the Euclidean algorithm, and of its
typesetting; - xintfrac, which computes fractions using xint; -
xintseries, which computes partial sums using xint; and -
xintcfrac, which deals with the computation of continued
fractions. All of the packages' computations are done in a way
that they can operate in an expanding environment. The packages
may be used either with Plain TeX or LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/xint/xint.sty
%{_texmfdistdir}/tex/generic/xint/xintbinhex.sty
%{_texmfdistdir}/tex/generic/xint/xintcfrac.sty
%{_texmfdistdir}/tex/generic/xint/xintexpr.sty
%{_texmfdistdir}/tex/generic/xint/xintfrac.sty
%{_texmfdistdir}/tex/generic/xint/xintgcd.sty
%{_texmfdistdir}/tex/generic/xint/xintseries.sty
%{_texmfdistdir}/tex/generic/xint/xinttools.sty
%doc %{_texmfdistdir}/doc/generic/xint/README
%doc %{_texmfdistdir}/doc/generic/xint/xint.pdf
#- source
%doc %{_texmfdistdir}/source/generic/xint/xint.dtx
%doc %{_texmfdistdir}/source/generic/xint/xint.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
