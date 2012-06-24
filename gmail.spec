Summary:	Gmail is an experimental sql based vfolder email system
Summary(pl):	Gmail - eksperymentlny, bazuj�cy na SQL system pocztowy z vfolderami
Name:		gmail
Version:	0.6.0
Release:	6
License:	GPL
Group:		X11/Applications
Source0:	http://gmail.linuxpower.org/%{name}-%{version}.tar.gz
# Source0-md5:	6dec954060841f8c62583cf8605f609c
Patch0:		%{name}-gnome-print_fix.patch
URL:		http://gmail.linuxpower.org/
BuildRequires:	esound-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	libglade-gnome-devel
BuildRequires:	mysql-devel >= 3.23
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gmail is an experimental sql based vfolder email system. It has the
following features:

Up to 255 vfolder views of the mail store. This is the main feature, I
originally got this idea from Miguel De Icaza. The idea is that you
keep all your mail in one big folder and:
 - approach it from different views (querys). It is a powerful way of
   approaching email management
 - 'matching' facility where messages that don't get caught by your
   custom vfolders are put into an 'Inbox' vfolder. A caching mechanism
   based on this 'matched index' also gives fast speeds
 - incoming POP3
 - outgoing SMTP
 - Drag'n'drop from gnomecard addressbook
 - Mbox export, import available through POP3
 - Sound events, configurable through the GNOME control centre

%description -l pl
Gmail to eksperymentalny, bazuj�cy na SQL, system pocztowy z
vfolderami. G��wna cecha to do 255 widok�w vfolder skrzynki pocztowej.
Idea pochodzi od Miguela de Icaza, polega na tym, �eby poczt� trzyma�
w jednym du�ym folderze i:
 - dostawa� si� do niej z r�nych widok�w (zapyta�)
 - u�atwienie 'matching', gdzie wiadomo�ci nie wy�apane przez vfoldery
   s� wrzucane do vfolderu Inbox; mechanizm buforuj�cy przyspiesza
   dzia�anie
 - odbieranie poczty przez POP3
 - wysy�anie poczty przez SMTP
 - obs�uga przeci�gnij-i-upu�� z ksi��ki adresowej gnomecard
 - eksport do formatu mbox, import mo�liwy poprzez POP3
 - zdarzenia d�wi�kowe konfigurowalne z GNOME Control Center

%prep
%setup -q
%patch -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Network/Mail

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS HACKING README* THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/sound/*
%{_applnkdir}/Network/Mail/*
%{_datadir}/gmail
