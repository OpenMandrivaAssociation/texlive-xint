Name:		texlive-xint
Version:	63562
Release:	2
Summary:	Expandable operations on long numbers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/xint
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xint.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xint.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xint.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides four packages: xint, which provides
expandable TeX macros that implement the basic arithmetic
operations of addition, subtraction, multiplication and
division, as applied to arbitrarily long numbers represented as
chains of digits with an optional minus sign; xinttools is
loaded by xint (hence by all other packages of the bundle,
too): it provides utilities of independent interest such as
expandable and non-expandable loops. xintfrac, which computes
fractions using xint; xintexpr, which extends xintfrac with an
expandable parser of expressions involving integers and a wide
variety of operators; xintbinhex provides conversions to and
from binary and hexadecimal bases; xintseries, which provides
basic functionality for computing partial sums using xint;
xintgcd, which provides implementations of the Euclidean
algorithm, and of its typesetting; xintcfrac, which deals with
the computation of continued fractions, All of the packages'
computations are done in a way that they can operate in an
expanding environment. The packages may be used either with
Plain TeX or LaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/xint
%doc %{_texmfdistdir}/doc/generic/xint
#- source
%doc %{_texmfdistdir}/source/generic/xint

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
