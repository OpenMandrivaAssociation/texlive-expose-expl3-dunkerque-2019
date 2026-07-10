%global tl_name expose-expl3-dunkerque-2019
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Using expl3 to implement some numerical algorithms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/expose-expl3-dunkerque-2019
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/expose-expl3-dunkerque-2019.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/expose-expl3-dunkerque-2019.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An article, in French, based on a presentation made in Dunkerque for the
"stage LaTeX" on 12 June 2019. The articles gives three examples of code
in expl3 with (lots of) comments: Knuth's algorithm to create a list of
primes, the sieve of Eratosthenes, Kaprekar sequences. The package
contains the code itself, the documentation as a PDF file, and all the
files needed to produce it.

