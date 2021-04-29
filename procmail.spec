#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : procmail
Version  : 3.22
Release  : 12
URL      : https://mirrors.kernel.org/debian/pool/main/p/procmail/procmail_3.22.orig.tar.gz
Source0  : https://mirrors.kernel.org/debian/pool/main/p/procmail/procmail_3.22.orig.tar.gz
Summary  : procmail mail delivery agent
Group    : Development/Tools
License  : GPL-2.0
Requires: procmail-bin = %{version}-%{release}
Requires: procmail-license = %{version}-%{release}
Requires: procmail-man = %{version}-%{release}
Patch1: CVE-2014-3618.patch
Patch2: fix_memory_allocation_bug.patch
Patch3: getline.patch
Patch4: mandir.patch
Patch5: CVE-2017-16844.patch

%description
Most mail servers such as sendmail need to have a local delivery agent.
Procmail can be used as the local delivery agent for you mail server.  It
supports a rich command set that allows you to pre-sort, archive, or re-mail
incoming mail automatically.  SmartList also needs procmail to operate.

%package bin
Summary: bin components for the procmail package.
Group: Binaries
Requires: procmail-license = %{version}-%{release}

%description bin
bin components for the procmail package.


%package license
Summary: license components for the procmail package.
Group: Default

%description license
license components for the procmail package.


%package man
Summary: man components for the procmail package.
Group: Default

%description man
man components for the procmail package.


%prep
%setup -q -n procmail-3.22
cd %{_builddir}/procmail-3.22
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604442168
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1604442168
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/procmail
cp %{_builddir}/procmail-3.22/COPYING %{buildroot}/usr/share/package-licenses/procmail/aac97ddcbe9232a375d87b7f09a54a9674fc8175
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/formail
/usr/bin/lockfile
/usr/bin/mailstat
/usr/bin/procmail

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/procmail/aac97ddcbe9232a375d87b7f09a54a9674fc8175

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/formail.1
/usr/share/man/man1/lockfile.1
/usr/share/man/man1/procmail.1
/usr/share/man/man5/procmailex.5
/usr/share/man/man5/procmailrc.5
/usr/share/man/man5/procmailsc.5
