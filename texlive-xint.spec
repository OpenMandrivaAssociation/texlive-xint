%global tl_name xint
%global tl_revision 76255

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4o
Release:	%{tl_revision}.1
Summary:	Expandable arbitrary precision floating point and integer operations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/xint
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xint.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xint.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xint.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Loading xintexpr provides \xinteval and \xintfloateval. \xintfloateval
evaluates numerical expressions. The floating point precision defaults
to 16 decimal digits and can be set by user. Trigonometry, exponential
and logarithms are implemented up to a maximal precision of 62 decimal
digits. \xinteval computes exactly with integers, fractions, and decimal
numbers or numbers in scientific notation. Note though that multiplying
two floating point numbers will about double the number of digits, and
so on, because the algebra is done exactly. Both are compatible with
expansion-only context. Loading xintexpr imports automatically various
other modules that it depends upon. Among them: xinttools: utilities
such as expandable and non-expandable loops, xint: macros implementing
in particular the basic operations on arbitrarily long integers,
xintbinhex: conversions between decimal and binary, octal, or
hexadecimal bases for arbitrarily long integers, xintfrac: macros
implementing in particular the basic operations on arbitrarily large
fractions, decimal numbers, or numbers in scientific notation. Further
modules of independent interest include xintgcd, xintseries and
xintcfrac. You can use xintexpr (and the other components) with LaTeX
(via \usepackage) or also with Plain TeX, OpTeX, or ConTeXt (via \input
xintexpr.sty). All the components are documented in the file xint.pdf,
which also contains the commented source code.

