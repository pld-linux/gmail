Summary:	Gmail is an experimental sql based vfolder email system
Name:		gmail
Version:	0.5.2
Release:	1
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	http://gmail.linuxpower.org/%{name}-%{version}.tar.gz
URL:		http://gmail.linuxpower.org/
BuildRequires:	esound-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfigdir	/etc/X11/GNOME

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
 - Sound events, configurable through the Gnome control centre

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Network/Mail

gzip -9nf ChangeLog AUTHORS HACKING README* THANKS TODO

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/sound/*
%{_applnkdir}/Network/Mail/*
