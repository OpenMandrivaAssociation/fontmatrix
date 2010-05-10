Name:           fontmatrix
Version:        0.6.0
Release:        %mkrel 1        
Summary:        featureful personal font manager
License:        GPL
Group:          Office
URL:            http://fontmatrix.net/
Source0:        http://fontmatrix.net/archives/fontmatrix-%{version}-Source.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  qt4-devel
BuildRequires:  freetype2
BuildRequires:  desktop-file-utils

%description
fontmatrix is a manager built with the kind of features and abilities graphic
designers, layout professionals along with others have felt necessary, but
modernized with some new touches. 

Fontmatrix has a concept of 'tagging'. This makes it really nice to group
fonts and even sub-group them logically for use in a book for instance. It
also has extensive gui support for showing all glyphs in a font, previews of
sample text, variable sizing and also tells what kinds of advanced Open Type
features are inside each font. These features have never been seen outside of
a font editor. And not least, it creates a nice PDF catalogue of user's fonts
for printing or reference. In short, fontmatrix is a font manager for
professionals, but is nice and user friendly.

%prep
%setup -q -n fontmatrix-%{version}-Source

%build
cmake . -DCMAKE_INSTALL_PREFIX:PATH=%{buildroot}/usr
make

%install
rm -rf %{buildroot}
make install
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/fontmatrix.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog TODO
%{_bindir}/fontmatrix
%{_mandir}/man1/fontmatrix.1*
%{_datadir}/applications/fontmatrix.desktop
%{_iconsdir}/hicolor/*/apps/fontmatrix.png
%dir %{_datadir}/fontmatrix
%{_datadir}/fontmatrix/*
