Summary:	Calcurse - text-based personal organizer
Summary(pl.UTF-8):	Calcurse - tekstowy organizer
Name:		calcurse
Version:	2.9.2
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://calcurse.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	5cb7d9c9edddc551fc62c9c5733591c5
URL:		http://calcurse.org/
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

%build
%configure \
	CPPFLAGS="%{rpmcppflags} $(pkg-config --cflags ncursesw)"
	LDFLAGS="%{rpmldflags} $(pkg-config --libs ncursesw)"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS doc/* TODO NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
