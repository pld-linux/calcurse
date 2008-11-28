Summary:	Calcurse - text-based personal organizer
Summary(pl.UTF-8):	Calcurse - tekstowy organizer
Name:		calcurse
Version:	2.3
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://culot.org/cgi-bin/get.cgi?%{name}-%{version}.tar.gz
# Source0-md5:	3aaa2f788238a837df0cf137f3657567
URL:		http://culot.org/calcurse/
BuildRequires:	ncurses-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calcurse is a text-based personal organizer which helps keeping track
of events and everyday tasks. It contains a calendar, a 'todo' list,
and puts your appointments in order. The user interface is
configurable, and one can choose between different color schemes and
layouts. All of the commands are documented within an online help
system.

%description -l pl.UTF-8
Calcurse jest tekstowym organizerem, który pomaga w śledzeniu
codziennych czynności. Zawiera kalendarz, listę zadań do zrobienia
"todo", potrafi uporządkować listę spotkań. Interfejs użytkownika jest
konfigurowalny i można wybrać jeden ze schematów kolorowania i układu
okien. Wszystkie komendy programu są udokumentowane w systemie pomocy
online.

%prep
%setup -q
%{__sed} -i -e 's/#include <ncurses.h>/#include <ncurses\/ncurses.h>/' src/*{c,h}
%{__sed} -i -e 's/ncurses\.h/ncurses\/ncurses.h/' configure

%build
%configure

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS doc/* ChangeLog TODO NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
