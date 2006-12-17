#
Summary:	Calcurse - text-based personal organizer
Summary(pl):	Calcurse - tekstowy organizer
Name:		calcurse
Version:	1.6
Release:	1
License:	GPL v2
Group:		Applications
Source0:	ftp://ftp.pld-linux.org/people/piotrek/src/%{name}-%{version}.tar.gz
# Source0-md5:	9c790622c163e664a380334d43d40796
URL:		http://culot.org/calcurse/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calcurse is a text-based personal organizer which helps keeping track
of events and everyday tasks. It contains a calendar, a 'todo' list,
and puts your appointments in order. The user interface is
configurable, and one can choose between different color schemes and
layouts. All of the commands are documented within an online help
system.

%description -l pl
Calcurse jest tekstowym organizerem, który pomaga w ¶ledzeniu
codziennych czynno¶ci. Zawiera kalendarz, listê zadañ do zrobienia
"todo", potrafi uporz±dkowaæ listê spotkañ. Interfejs u¿ytkownika jest
konfigurowalny i mo¿na wybraæ jeden ze schematów kolorowania i uk³adu
okien. Wszystkie komendy programu s± udokumentowane w systemie pomocy
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
%doc doc/* ABOUT-NLS ChangeLog TODO NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
