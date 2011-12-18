%define release %mkrel 1

Name:		partclone
Version:	0.2.38
Release:	%{release}
Group:		System/Configuration/Other
URL:		http://partclone.sf.net
License:	GPLv2
Summary:	File System Clone Utilities
Source0:	%{name}_%{version}.tar.gz
Patch1:		partclone-0.2.38-mdv-libxfs.patch
BuildRequires:	e2fsprogs-devel
BuildRequires:	libntfs-devel
BuildRequires:	ncursesw-devel
BuildRoot:    %{_tmppath}/%{name}-build

%description
Partclone provides utilities to back up and restore used-blocks of a partition
and it is designed for higher compatibility of the file system by using
existing library, e.g. e2fslibs is used to read and write the ext2 partition.

Authors:
--------
    Thomas Tsai <Thomas _at_ nchc org tw>
    Jazz Wang <jazz _at_ nchc org tw>
    http://partclone.sourceforge.net 
    http://partclone.nchc.org.tw

%prep
%setup -q 
#patch1 -p1

%build
%configure \
	--enable-extfs \
	--enable-hfsp \
	--enable-fat \
	--enable-ntfs \
	--enable-btrfs \
	--enable-ncursesw
make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%doc %{_mandir}/man?/*
%{_sbindir}/*
