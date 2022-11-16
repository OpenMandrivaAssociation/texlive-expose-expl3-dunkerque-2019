Name:		texlive-expose-expl3-dunkerque-2019
Version:	54451
Release:	1
Summary:	Using expl3 to implement some numerical algorithms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/expose-expl3-dunkerque-2019
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expose-expl3-dunkerque-2019.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expose-expl3-dunkerque-2019.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
An article, in French, based on a presentation made in
Dunkerque for the "stage LaTeX" on 12 June 2019. The articles
gives three examples of code in expl3 with (lots of) comments:
Knuth's algorithm to create a list of primes, the sieve of
Eratosthenes, Kaprekar sequences. The package contains the code
itself, the documentation as a PDF file, and all the files
needed to produce it.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/expose-expl3-dunkerque-2019

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
