/* ============================================================
   Ali's Python Course — app logic
   Progress tracking is stored in localStorage so it survives
   refreshes, browser restarts, and works when deployed static.
   ============================================================ */

(function () {
  "use strict";

  var KEY = "ali-python-course.progress.v1";

  /* ---------- storage ---------- */

  function readProgress() {
    try {
      var raw = localStorage.getItem(KEY);
      if (!raw) return { done: {} };
      var parsed = JSON.parse(raw);
      if (!parsed || typeof parsed !== "object") return { done: {} };
      if (!parsed.done || typeof parsed.done !== "object") parsed.done = {};
      return parsed;
    } catch (e) {
      return { done: {} };
    }
  }

  function writeProgress(p) {
    try {
      localStorage.setItem(KEY, JSON.stringify(p));
      return true;
    } catch (e) {
      return false;
    }
  }

  var state = readProgress();

  function isDone(id) { return !!state.done[id]; }

  function setDone(id, val) {
    if (val) state.done[id] = Date.now();
    else delete state.done[id];
    writeProgress(state);
    refreshAll();
  }

  /* ---------- course order comes from the sidebar DOM ---------- */

  function courseOrder() {
    var out = [];
    var items = document.querySelectorAll(".nav-item[data-id]");
    for (var i = 0; i < items.length; i++) {
      out.push({
        id: items[i].getAttribute("data-id"),
        label: items[i].getAttribute("data-label") || "",
        href: items[i].getAttribute("href")
      });
    }
    return out;
  }

  function countDone() {
    var order = courseOrder();
    var n = 0;
    for (var i = 0; i < order.length; i++) if (isDone(order[i].id)) n++;
    return { done: n, total: order.length };
  }

  function pct(done, total) {
    if (total <= 0) return 0;
    return Math.round((done / total) * 100);
  }

  var CHEERS = [
    "You are on fire!",
    "Coding legend in the making!",
    "Keep going, hero!",
    "Python power rising!",
    "One lesson at a time!",
    "Ali the Code Master!"
  ];

  function cheer() {
    return CHEERS[Math.floor(Math.random() * CHEERS.length)];
  }

  /* ---------- refresh every progress-aware element ---------- */

  function refreshAll() {
    var c = countDone();
    var p = pct(c.done, c.total);

    // sidebar
    var sbBar = document.getElementById("sb-bar");
    var sbPct = document.getElementById("sb-pct");
    var sbCount = document.getElementById("sb-count");
    var sbCheer = document.getElementById("sb-cheer");
    if (sbBar) sbBar.style.width = p + "%";
    if (sbPct) sbPct.textContent = p + "%";
    if (sbCount) sbCount.textContent = c.done + " / " + c.total + " lessons";

    // topbar mini
    var mbBar = document.getElementById("mb-bar");
    var mbTxt = document.getElementById("mb-txt");
    if (mbBar) mbBar.style.width = p + "%";
    if (mbTxt) mbTxt.textContent = p + "%";

    // hero (home page)
    var hBar = document.getElementById("hero-bar");
    var hPct = document.getElementById("hero-pct");
    var hRow = document.getElementById("hero-row2-count");
    var hNext = document.getElementById("hero-next");
    if (hBar) hBar.style.width = p + "%";
    if (hPct) hPct.textContent = p + "%";
    if (hRow) hRow.textContent = c.done + " of " + c.total + " lessons complete";

    // per-item checkmarks
    var items = document.querySelectorAll(".nav-item[data-id]");
    for (var i = 0; i < items.length; i++) {
      var it = items[i];
      var id = it.getAttribute("data-id");
      var dot = it.querySelector(".nav-dot");
      if (isDone(id)) {
        it.classList.add("done");
        if (dot) dot.textContent = "\u2713";
      } else {
        it.classList.remove("done");
        if (dot) dot.textContent = "";
      }
    }

    // home page cards
    var cards = document.querySelectorAll(".card[data-id]");
    for (var j = 0; j < cards.length; j++) {
      var cd = cards[j];
      var cid = cd.getAttribute("data-id");
      var st = cd.querySelector(".state");
      if (isDone(cid)) {
        cd.classList.add("done");
        if (st) st.innerHTML = '<span class="here">\u2713</span> Completed!';
      } else {
        cd.classList.remove("done");
        if (st) st.innerHTML = "Start lesson \u2192";
      }
    }

    // "next incomplete lesson" pointer on home
    if (hNext) {
      var found = null;
      for (var k = 0; k < courseOrder().length; k++) {
        if (!isDone(courseOrder()[k].id)) { found = courseOrder()[k]; break; }
      }
      if (found) {
        hNext.textContent = found.label;
        hNext.setAttribute("href", found.href);
      } else {
        hNext.textContent = "Course complete \u2014 you did it! \u{1F3C6}";
        hNext.setAttribute("href", "#");
      }
    }

    // current lesson complete button
    var btn = document.getElementById("complete-btn");
    if (btn) {
      var myId = btn.getAttribute("data-id");
      if (isDone(myId)) {
        btn.classList.remove("primary");
        btn.classList.add("success");
        btn.innerHTML = '<span>\u2713</span> Lesson Completed';
        btn.setAttribute("aria-pressed", "true");
      } else {
        btn.classList.remove("success");
        btn.classList.add("primary");
        btn.innerHTML = '<span>\u2b50</span> Mark This Lesson Complete';
        btn.setAttribute("aria-pressed", "false");
      }
    }

    // milestone / finish banners
    var fin = document.getElementById("finish-banner");
    if (fin) fin.style.display = c.done === c.total && c.total > 0 ? "block" : "none";

    if (sbCheer) sbCheer.textContent = c.done === 0 ? "Ready to start!" : cheer();
  }

  /* ---------- confetti ---------- */

  function celebrate() {
    var colors = ["#ffd43b", "#58a6ff", "#3fb950", "#a371f7", "#f778ba", "#ff9f45"];
    var box = document.createElement("div");
    box.className = "confetti";
    for (var i = 0; i < 70; i++) {
      var piece = document.createElement("i");
      piece.style.left = Math.random() * 100 + "vw";
      piece.style.background = colors[Math.floor(Math.random() * colors.length)];
      piece.style.animationDuration = 2.2 + Math.random() * 1.8 + "s";
      piece.style.animationDelay = Math.random() * 0.5 + "s";
      piece.style.transform = "rotate(" + Math.random() * 360 + "deg)";
      box.appendChild(piece);
    }
    document.body.appendChild(box);
    setTimeout(function () {
      if (box.parentNode) box.parentNode.removeChild(box);
    }, 4600);
  }

  /* ---------- toast ---------- */

  var toastTimer = null;
  function toast(msg, isMilestone) {
    var t = document.getElementById("toast");
    if (!t) {
      t = document.createElement("div");
      t.id = "toast";
      t.className = "toast";
      document.body.appendChild(t);
    }
    t.textContent = msg;
    t.style.borderLeftColor = isMilestone ? "#ffd43b" : "#3fb950";
    t.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { t.classList.remove("show"); }, 2800);
  }

  /* ---------- wire up ---------- */

  function init() {
    refreshAll();

    // mobile nav toggle
    var menuBtn = document.getElementById("menu-btn");
    if (menuBtn) {
      menuBtn.addEventListener("click", function () {
        document.body.classList.toggle("nav-open");
      });
    }
    document.addEventListener("click", function (e) {
      if (!document.body.classList.contains("nav-open")) return;
      var tag = e.target;
      if (tag.closest && tag.closest(".sidebar")) return;
      if (tag.closest && tag.closest(".menu-btn")) return;
      document.body.classList.remove("nav-open");
    });

    // complete toggle
    var btn = document.getElementById("complete-btn");
    if (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-id");
        var wasDone = isDone(id);
        setDone(id, !wasDone);

        if (!wasDone) {
          var c = countDone();
          var p = pct(c.done, c.total);
          if (p === 100) {
            celebrate();
            toast("\u{1F3C6} COURSE COMPLETE! You are a Python champion, Ali!", true);
          } else {
            celebrate();
            toast("\u2b50 Nice work! " + p + "% of the course complete!");
          }
        } else {
          toast("Marked as not finished. You can redo it anytime!");
        }
      });
    }

    // copy buttons on code blocks
    var copies = document.querySelectorAll(".copy-btn");
    for (var i = 0; i < copies.length; i++) {
      copies[i].addEventListener("click", function () {
        var self = this;
        var block = self.closest(".code-block");
        var code = block ? block.querySelector("pre code") : null;
        if (!code) return;
        var text = code.innerText;
        function ok() {
          self.classList.add("copied");
          self.textContent = "Copied!";
          setTimeout(function () {
            self.classList.remove("copied");
            self.textContent = "Copy";
          }, 1600);
        }
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(ok, function () { fallback(text, ok); });
        } else {
          fallback(text, ok);
        }
      });
    }

    function fallback(text, cb) {
      try {
        var ta = document.createElement("textarea");
        ta.value = text;
        ta.setAttribute("readonly", "");
        ta.style.position = "fixed";
        ta.style.opacity = "0";
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        document.body.removeChild(ta);
        cb();
      } catch (e) { /* ignore */ }
    }

    // reset
    var reset = document.getElementById("reset-btn");
    if (reset) {
      reset.addEventListener("click", function () {
        if (window.confirm("Reset ALL progress? Every checkmark will be cleared.")) {
          state = { done: {} };
          writeProgress(state);
          refreshAll();
          toast("Progress reset. Fresh start!");
        }
      });
    }

    // cross-tab sync
    window.addEventListener("storage", function (e) {
      if (e.key === KEY) {
        state = readProgress();
        refreshAll();
      }
    });

    // keyboard shortcut: "c" completes current lesson
    document.addEventListener("keydown", function (e) {
      var tag = (e.target.tagName || "").toLowerCase();
      if (tag === "input" || tag === "textarea" || e.target.isContentEditable) return;
      if (e.metaKey || e.ctrlKey || e.altKey) return;
      if (e.key === "c" || e.key === "C") {
        var b = document.getElementById("complete-btn");
        if (b) b.click();
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
