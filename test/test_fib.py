import datetime, os
from spotify import luigi

# Calculates Fibonacci numbers :)

@luigi.expose
class Fib(luigi.Task):
    n = luigi.IntParameter(default = 100)

    def requires(self):
        if self.n > 2: return [Fib(self.n - 1), Fib(self.n - 2)]
        else: return []

    def output(self):
        return luigi.File('/tmp/fib_%d' % self.n)

    def run(self):
        if self.n == 0:
            s = 1
        elif self.n == 1:
            s = 1
        else:
            s = 0
            for input in self.input():
                for line in input.open('r'):
                    s += int(line.strip())

        print 'F_%d = %d' % (self.n, s)
        self.output().open('w').write('%d\n' % s)
        import time
        time.sleep(1)

if __name__ == '__main__':
    luigi.run()