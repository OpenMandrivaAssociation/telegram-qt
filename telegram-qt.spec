%define version_major 0
%define version_minor 2
%define version_patch 0


%define telegramqt5 %mklibname telegram-qt5 %{version_major}
%define telegramqtd %mklibname telegram-qt5 -d
%define date 20190421


Name: telegram-qt
Summary: Qt library for Telegram network
Version: %{version_major}.%{version_minor}.%{version_patch}
Release: 1
Group: System/Libraries
License: LGPLv2.1
URL: https://github.com/Kaffeine/telegram-qt
Source0: telegram-qt-%{version}-%{date}.tar.xz
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(openssl)
BuildRequires: cmake
BuildRequires: qmake5

%description
%{summary}.

%package -n %{telegramqt5}
Summary: Qt library for Telegram network
Requires: openssl

%description -n %{telegramqt5}
%{summary}.

%package -n %{telegramqtd}
Summary:    Development headers and pkg-config for TelegramQt library
Group:      Development/Libraries
Requires:   %{telegramqt5} = %{EVRD}
Requires:   qt5-qtbase-devel

%description -n %{telegramqtd}
%{summary}.

%prep
%autosetup -n %{name}-%{version}-%{date}

%build
%cmake \
    -DENABLE_TESTAPP=FALSE \
    -DBUILD_VERSION="%{version}"

%make_build

%install
%make_install -C build

%files -n %{telegramqt5}
%{_libdir}/libTelegramQt5.so.%{version_major}.%{version_minor}
%{_libdir}/libTelegramQt5.so.%{version_major}.%{version_minor}.%{version_patch}
%{_libdir}/qt5/qml/TelegramQt/qmldir
%{_libdir}/qt5/qml/TelegramQt/libTelegramQmlPlugin.so
%{_libdir}/libTelegramQt5Qml.so.%{version_major}.%{version_minor}
%{_libdir}/libTelegramQt5Qml.so.%{version_major}.%{version_minor}.%{version_patch}

%files -n %{telegramqtd}
%dir %{_includedir}/TelegramQt5
%dir %{_includedir}/TelegramQt5/TelegramQt
%dir %{_libdir}/cmake/TelegramQt5
%dir %{_libdir}/pkgconfig
%{_includedir}/TelegramQt5/TelegramQt/*
%{_libdir}/libTelegramQt5.so
%{_libdir}/cmake/TelegramQt5/TelegramQt5Config.cmake
%{_libdir}/cmake/TelegramQt5/TelegramQt5ConfigVersion.cmake
%{_libdir}/pkgconfig/TelegramQt5.pc
%{_libdir}/qt5/qml/TelegramQt/plugins.qmltypes
%{_libdir}/libTelegramQt5Qml.so
