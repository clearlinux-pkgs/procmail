#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : procmail
Version  : 3.22
Release  : 2
URL      : ftp://ftp.ucsb.edu/pub/mirrors/procmail/procmail-3.22.tar.gz
Source0  : ftp://ftp.ucsb.edu/pub/mirrors/procmail/procmail-3.22.tar.gz
Summary  : procmail mail delivery agent
Group    : Development/Tools
License  : GPL-2.0
Requires: procmail-bin
Requires: procmail-doc
Patch1: mandir.patch
Patch2: getline.patch

%description
Most mail servers such as sendmail need to have a local delivery agent.
Procmail can be used as the local delivery agent for you mail server.  It
supports a rich command set that allows you to pre-sort, archive, or re-mail
incoming mail automatically.  SmartList also needs procmail to operate.

%package bin
Summary: bin components for the procmail package.
Group: Binaries

%description bin
bin components for the procmail package.


%package doc
Summary: doc components for the procmail package.
Group: Documentation

%description doc
doc components for the procmail package.


%prep
%setup -q -n procmail-3.22
%patch1 -p1
%patch2 -p1

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/formail
/usr/bin/lockfile
/usr/bin/mailstat
/usr/bin/procmail

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
