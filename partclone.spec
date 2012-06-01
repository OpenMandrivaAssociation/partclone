Name:		partclone
Version:	0.2.48
Release:	%mkrel 1
Group:		System/Configuration/Other
URL:		http://partclone.sf.net
License:	GPLv2
Summary:	File System Clone Utilities
Source0:	http://downloads.sourceforge.net/project/partclone/stable/%{version}/%{name}-%{version}.tar.gz
Patch1:		partclone-0.2.38-mdv-libxfs.patch
BuildRequires:	ext2fs-devel
BuildRequires:	libntfs-devel
BuildRequires:	ncursesw-devel
BuildRequires:	ncurses-devel
BuildRequires:	libuuid-devel

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
%make

%install
%makeinstall_std
%find_lang %name

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO
%doc %{_mandir}/man?/*
%{_sbindir}/*
