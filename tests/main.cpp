#include <QTest>

#include "testqstring.h"
#include "testfoo.h"

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    int t1 = QTest::qExec(new TestFoo, argc, argv);
    int t2 = QTest::qExec(new TestQString, argc, argv);

    return std::max(t1,t2);
}
