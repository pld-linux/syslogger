# TODO: optflags
Summary:	Copy lines from stdin to syslog
Summary(pl.UTF-8):	Kopiowanie linii ze standardowego wejścia do sysloga
Name:		syslogger
Version:	1.03
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://www.nb.net/~lbudney/linux/software/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	87ce704b92e6e1996aaacbf3f6b3a579
Patch0:		%{name}-home.patch
URL:		http://www.pobox.com/~lbudney/linux/software/syslogger.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Syslogger copies lines from the standard input, and logs them to
syslog.

%description -l pl.UTF-8
Syslogger kopiuje linie ze standardowego wejścia i zapisuje je do
sysloga.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
