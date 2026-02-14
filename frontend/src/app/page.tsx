import NewsList from "@/components/NewsList";

export default function Home() {
  return (
    <main className="min-h-screen bg-pink-50/30 py-8">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 tracking-tight">
            HN Reader
          </h1>
          <p className="mt-2 text-gray-600">
            Top stories from Hacker News, ingested into MySQL.
          </p>
        </header>

        <NewsList />

        <footer className="mt-12 text-center text-sm text-gray-500 pb-8">
          <p>Built with Next.js, MySQL, and Python</p>
        </footer>
      </div>
    </main>
  );
}
