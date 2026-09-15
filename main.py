"""Find the words hidden in a grid of letters, against the clock.

The grid is not random letters. Truly random letters produce grids with
almost no words in them, which is not a hard game - it is a broken one. So
the letters are drawn from a distribution weighted the way English actually
uses them, and vowels are guaranteed a minimum share.

Words must be traceable through ADJACENT tiles, each used once, which is what
stops it being a list of words that happen to share letters.

The dictionary is built in. No network, no downloads.
"""
import random
import tkinter as tk

import mavis_ui

FEATURE = "word-grid"

SIZE = 4
ROUND_SECONDS = 180
MIN_LENGTH = 3

# Letter frequencies as English actually uses them, so grids contain words.
# Uniform random letters give grids full of J, Q, X and V and nothing to find.
WEIGHTED = ("aaaaaaaaa" "bb" "ccc" "dddd" "eeeeeeeeeeee" "ffff" "ggg" "hhhhhh"
            "iiiiiiiii" "j" "k" "llll" "mmm" "nnnnnnn" "ooooooo" "pp" "q"
            "rrrrrr" "sssssss" "tttttttttt" "uuu" "v" "ww" "x" "yyy" "z")

WORDS = set("""
ace ache acid acre act acts add ado aft age aged ages ago aid aide aids ail
aim air airs ale ali all also alt amid among amp and ant ante ants any ape
apes apt arc arch arcs are area arm arms army art arts ash aside ask asked
ate atom attic aunt auto awe axe aye back bad bade bag bags bail bait bake
bald bale ball balm band bane bang bank bar bard bare barn bars base bash
bat bath bats bay bead beam bean bear beat bed bee been beer beg bell belt
bend bent best bet bid big bike bile bill bin bind bird bit bite blade blame
bland blast blend blind blond blot blue boa board boast boat bode body bog
boil bold bolt bond bone book boom boot bore born boss both bout bow bowl
box boy brad brag braid brain brand brass brave bread break bred brick bride
brief bring broad broil broke brook broom brother brown brush bud bug bulb
bulk bull bump bun bunch bundle bunk burn burst bus bush bust busy but buy
cab cabin cable cage cake calf call calm came camp can cane cap cape car
card care carry cart case cash cast cat catch cause cave cell cent chain
chair chalk chant chap charm chart chase chat cheap cheat check cheek cheer
chest chew chief child chill chin chip choice choke chop chose cider cigar
circle cite city claim clam clan clap clash class claw clay clean clear clerk
click cliff climb cling cloak clock clog close cloth cloud club clue coach
coal coast coat code coil coin cold collar colt comb come cone cook cool
cope copy cord core cork corn cost cot couch cough could count court cove
cow crab crack craft cram crane crash crate crawl cream creek crest crew crib
cried crime crisp croak crop cross crowd crown crude cruel crumb crush crust
cry cub cube cue cuff cup curb cure curl curse curve cut dab dad daily dairy
dam damp dance dare dark dart dash date dawn day dead deaf deal dean dear
debt decay deck deed deep deer delay dent deny desk dial dice diet dig dim
dine dip dirt dish disk ditch dive dock does dog doll dome done door dose
dot doubt dough dove down doze drab draft drag drain drama drank draw dread
dream dress dried drift drill drink drip drive drop drove drown drug drum
dry duck due dug dull dumb dump dune dusk dust duty dwell dye each eager
eagle ear earl early earn earth ease east easy eat echo edge edit eel egg
eight elbow elder elf elk else empty end enemy enjoy enter entry equal error
even event ever every evil exact exam exit extra eye face fact fade fail
faint fair faith fall false fame fan far farm fast fat fate fault fear feast
feat fed fee feed feel feet fell felt fence fern few field fierce fifth fig
fight file fill film filth final find fine finger fire firm first fish fist
fit five fix flag flake flame flap flash flat flaw fled flee flesh flew
flight fling flint flip float flock flood floor flour flow fluid flute fly
foam focus fog fold folk fond food fool foot for force ford fork form fort
forth found four fox frame free fresh fried friend frog from front frost
frown fruit fry fuel full fun fund fur fuse gain gale game gang gap garden
gas gate gave gaze gear gem gene gift girl give glad gland glare glass gleam
glide globe gloom glory glove glow glue goal goat gold golf gone good goose
gown grab grace grade grain grand grant grape grasp grass grave gray graze
great greed green greet grew grid grief grill grim grin grind grip groan
groom groove group grove grow growl grown gruff guard guess guest guide
guild guilt gulf gull gum gun gust gut hail hair half hall halt ham hand
hang harm harsh haste hat hatch hate haul have hawk hay haze head heal heap
hear heart heat heavy heel held hell helm help hem hen herb herd here hero
hid hide high hike hill him hind hinge hint hire his hit hive hoax hold hole
holy home hone honey honk hood hoof hook hoop hope horn horse hose host hot
hound hour house howl huge hug hull human humid hump hung hunt hurl hurry
hurt hush hut ice icy idea idle inch ink inn iron item ivory jab jail jam
jar jaw jazz jeep jelly jet jewel job join joke jolly jolt joy judge juice
jump junk jury just keel keen keep kept key kick kid kill kin kind king kiss
kit kite knee kneel knew knife knit knob knock knot know lab lace lack lad
ladder lady laid lake lamb lame lamp land lane lap lard large lash last late
laugh launch lava law lawn lay layer lazy lead leaf leak lean leap learn
lease least leave led ledge left leg lemon lend length lens lent less lesson
let level lever liar lice lick lid lie life lift light like limb lime limit
limp line link lion lip liquid list live load loaf loan lobby local lock
lodge loft log logic lone long look loom loop loose lord lose loss lost lot
loud love low loyal luck lump lunch lung lure lurk mad made magic maid mail
main major make male mall malt man mane many map marble march mare mark
market marsh mask mass mast mat match mate math maze meal mean meat medal
meet melt mend menu mercy mere merge merit merry mesh mess metal meter mice
mid might mild mile milk mill mind mine mint minus mist mix moan moat mob
mock mode moist mold mole money monk month mood moon moral more morn moss
most moth motor mound mount mourn mouse mouth move much mud mule mug music
must mute nail name nap napkin nation near neat neck need needle neigh nerve
nest net never new news next nice night nine noble nod noise none noon nor
north nose not note noun novel now numb nurse nut oak oar oat obey ocean odd
odor off offer often oil old olive once one onion only onto open opera orbit
order organ other ought ounce our out oval oven over owe owl own pace pack
pad page paid pail pain paint pair pale palm pan panel panic pants paper
parade parcel pardon park part party pass past paste pat patch path patio
pause pave paw pay peace peach peak pear pearl peck peel peer peg pen pencil
penny people pepper perch peril period pest pet phase phone photo piano pick
picnic pie piece pier pig pile pill pilot pin pinch pine pink pint pipe pit
pitch pity place plain plan plane plank plant plate play plea plot plow plug
plum plus pocket poem poet point poise poke pole polish poll pond pony pool
poor pop porch pore pork port pose post pot pouch pound pour powder power
praise pray press pretty price pride prince print prize probe profit prompt
proof proud prove prune public pull pulp pulse pump punch pupil pure purple
purse push put puzzle quart queen quest quick quiet quill quilt quit quite
quiz quote race rack radio raft rag rage raid rail rain raise rake ram ramp
ran ranch range rank rapid rare rash rat rate ratio raw ray razor reach read
ready real reap rear reason rebel recall recent recipe record reduce reed
reef reel refer reform region regret reign rein relax relay relief remain
remark remedy remind remove rent repair repeat reply report rescue resist
resort rest result retire return reveal review reward rhyme rib ribbon rice
rich rid ride ridge rifle right rigid rim ring rinse riot rip ripe rise risk
rival river road roar roast robe robin rock rod rode rogue role roll roof
room root rope rose rot rough round rouse route row royal rub rug ruin rule
rumor run rung runs rural rush rust sack sad saddle safe sage said sail
saint sake salad sale salt same sand sang sank sap sash sat sauce save saw
say scale scan scar scarf scene scent school scold scoop scope score scorn
scout scrap screen screw script scrub sea seal seam search season seat second
secret sect see seed seek seem seen seize seldom select self sell send sense
sent serve set seven sew shade shaft shake shall shame shape share shark
sharp shave shawl she shed sheep sheer sheet shelf shell shield shift shine
ship shirt shock shoe shone shook shoot shop shore short shot should shout
shove show shower shrank shred shrub shut shy sick side siege sigh sight sign
silk sill silly silver simple since sing sink sir sit site six size skate
sketch ski skid skill skin skip skirt skull sky slab slam slant slap slate
slave sled sleep sleeve slept slice slid slide slight slim sling slip slit
slope slot slow slug slum small smart smash smell smile smoke smooth snack
snail snake snap snare snatch sneak sniff snow snug soak soap soar sob
social sock soda sofa soft soil sold sole solid solve some son song soon
sore sorrow sort soul sound soup sour south sow space spade span spare spark
speak spear speed spell spend spent spice spill spin spine spire spirit spit
spite splash split spoil spoke sponge spoon sport spot spray spread spring
sprint spur spy square squeeze stab stable stack staff stage stain stair
stake stale stalk stall stamp stand star stare start state stay steady steak
steal steam steel steep steer stem step stick stiff still sting stir stock
stole stone stood stool stoop stop store storm story stout stove straw stray
streak stream street stress strict strike string strip stroke strong struck
stub stuck study stuff stump stun style sugar suit sum summer sun sung sunk
super sure surf swallow swam swamp swan swap swarm sway swear sweat sweep
sweet swell swept swift swim swing switch sword swore table tack tact tag
tail take tale talk tall tame tan tank tap tape target task taste taught tax
tea teach team tear tease teeth tell temper ten tend tent term test text
than thank that thaw the theft their them then there these they thick thief
thin thing think third thirst this thorn those though thread three threw
thrill throat throne throw thumb thus tick ticket tide tidy tie tiger tight
tile till tilt time tin tiny tip tire title toad toast today toe together
told toll tomb tone tongue tonight too took tool tooth top topic torch tore
toss total touch tough tour toward towel tower town toy trace track trade
trail train trap trash tray tread treat tree trial tribe trick tried trim
trip troop trot trouble truck true trunk trust truth try tub tube tuck tug
tulip tumble tune tunnel turn twice twig twin twist two type ugly umbrella
uncle under union unit unite until upon upper upset urge use used useful
usual vague vain vale valley value valve van vane vanish vapor vase vast
veil vein vent verb verse very vessel vest vice view vine violet virtue
visit vital voice void volume vote vow wade wag wage wagon waist wait wake
walk wall wander want war ward ware warm warn warp wash wasp waste watch
water wave wax way weak wealth wear weave web wed wedge weed week weep weigh
weird welcome weld well went were west wet whale what wheat wheel when where
which while whip whirl whisk white who whole whom whose why wick wide widow
width wife wig wild will win wind wine wing wink winter wipe wire wise wish
wit witch with wolf woman won wonder wood wool word wore work world worm
worn worry worse worth would wound wrap wreck wrist write wrong wrote yard
yarn yawn year yeast yell yellow yes yet yield yoke young your youth zeal
zebra zero zone zoo
""".split())


def new_grid():
    """Letters weighted to English, with vowels guaranteed."""
    while True:
        letters = [random.choice(WEIGHTED) for _ in range(SIZE * SIZE)]
        vowels = sum(1 for c in letters if c in "aeiou")
        # A grid with two vowels in sixteen tiles is unplayable. Five is
        # roughly what a good Boggle set gives you.
        if 4 <= vowels <= 8:
            return letters


def traceable(word, letters):
    """Can the word be walked through adjacent tiles, each used once?"""
    def neighbours(index):
        row, column = divmod(index, SIZE)
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == dc == 0:
                    continue
                r, c = row + dr, column + dc
                if 0 <= r < SIZE and 0 <= c < SIZE:
                    yield r * SIZE + c

    def walk(position, index, used):
        if index == len(word):
            return True
        for nxt in neighbours(position):
            if nxt not in used and letters[nxt] == word[index]:
                if walk(nxt, index + 1, used | {nxt}):
                    return True
        return False

    return any(letters[start] == word[0] and walk(start, 1, {start})
               for start in range(SIZE * SIZE))


def score_for(word):
    return {3: 1, 4: 1, 5: 2, 6: 3, 7: 5}.get(len(word), 11)


class App(mavis_ui.MavisWindow):
    def __init__(self):
        super().__init__(FEATURE, "Word Grid", width=460, height=600)
        state = mavis_ui.load_state(FEATURE, default={})
        self.best = int(state.get("best", 0))

        self.letters = new_grid()
        self.found = []
        self.score = 0
        self.remaining = ROUND_SECONDS
        self.ticking = None

        head = tk.Frame(self.content, bg=mavis_ui.INK)
        head.pack(fill="x", padx=18, pady=(16, 8))
        self.clock = tk.Label(head, text="3:00", bg=mavis_ui.INK,
                              fg=mavis_ui.GLOW, font=("Segoe UI", 20, "bold"))
        self.clock.pack(side="left")
        self.points = tk.Label(head, text="0", bg=mavis_ui.INK,
                               fg=mavis_ui.TEXT, font=("Segoe UI", 20, "bold"))
        self.points.pack(side="right")

        self.board = tk.Frame(self.content, bg=mavis_ui.INK)
        self.board.pack(padx=18)
        self.tiles = []
        for index in range(SIZE * SIZE):
            tile = tk.Label(self.board, text=self.letters[index].upper(),
                            bg=mavis_ui.PANEL, fg=mavis_ui.TEXT,
                            font=("Segoe UI", 20, "bold"), width=3, height=1)
            tile.grid(row=index // SIZE, column=index % SIZE, padx=3, pady=3)
            self.tiles.append(tile)

        self.entry = tk.Entry(self.content, bg=mavis_ui.PANEL,
                              fg=mavis_ui.GLOW, relief="flat",
                              insertbackground=mavis_ui.GLOW,
                              font=mavis_ui.mono(14), justify="center")
        self.entry.pack(fill="x", padx=18, pady=12, ipady=6)
        self.entry.bind("<Return>", lambda e: self.submit())
        self.entry.focus_set()

        self.message = tk.Label(self.content, text="Type a word and press enter.",
                                bg=mavis_ui.INK, fg=mavis_ui.DIM,
                                font=("Segoe UI", 10))
        self.message.pack()

        self.words = tk.Text(self.content, height=8, bg=mavis_ui.PANEL,
                             fg=mavis_ui.DIM, relief="flat",
                             font=mavis_ui.mono(9), wrap="word")
        self.words.pack(fill="both", expand=True, padx=18, pady=10)

        row = tk.Frame(self.content, bg=mavis_ui.INK)
        row.pack(pady=(0, 14))
        self.start_button = mavis_ui.button(row, "Start", self.start, accent=True)
        self.start_button.pack(side="left")
        mavis_ui.button(row, "New grid", self.reset).pack(side="left", padx=8)
        self.record = tk.Label(row, text="best %d" % self.best, bg=mavis_ui.INK,
                               fg=mavis_ui.DIM, font=("Segoe UI", 9))
        self.record.pack(side="left", padx=10)

    def start(self):
        if self.ticking:
            return
        self.tick()

    def tick(self):
        if self.remaining <= 0:
            self.finish()
            return
        minutes, seconds = divmod(self.remaining, 60)
        self.clock.configure(
            text="%d:%02d" % (minutes, seconds),
            fg=mavis_ui.BAD if self.remaining <= 15 else mavis_ui.GLOW)
        self.remaining -= 1
        self.ticking = self.after(1000, self.tick)

    def finish(self):
        if self.ticking:
            self.after_cancel(self.ticking)
            self.ticking = None
        self.clock.configure(text="0:00", fg=mavis_ui.BAD)
        if self.score > self.best:
            self.best = self.score
            mavis_ui.save_state(FEATURE, {"best": self.best})
            self.record.configure(text="best %d" % self.best)
            self.message.configure(text="Time. A new best score.",
                                   fg=mavis_ui.GOOD)
        else:
            self.message.configure(text="Time. You scored %d." % self.score,
                                   fg=mavis_ui.WARN)

    def submit(self):
        word = self.entry.get().strip().lower()
        self.entry.delete(0, "end")
        if not word:
            return
        if self.remaining <= 0:
            self.message.configure(text="The round is over.", fg=mavis_ui.WARN)
            return
        if len(word) < MIN_LENGTH:
            self.message.configure(text="Too short — three letters at least.",
                                   fg=mavis_ui.WARN)
        elif word in self.found:
            self.message.configure(text="Already had that one.", fg=mavis_ui.WARN)
        elif word not in WORDS:
            self.message.configure(text="Not in the dictionary.", fg=mavis_ui.BAD)
        elif not traceable(word, self.letters):
            self.message.configure(text="Not traceable through the grid.",
                                   fg=mavis_ui.BAD)
        else:
            points = score_for(word)
            self.score += points
            self.found.append(word)
            self.points.configure(text=str(self.score))
            self.words.insert("1.0", "%-14s +%d\n" % (word, points))
            self.message.configure(text="Good — %d point%s."
                                        % (points, "" if points == 1 else "s"),
                                   fg=mavis_ui.GOOD)
            if not self.ticking:
                self.start()

    def reset(self):
        if self.ticking:
            self.after_cancel(self.ticking)
            self.ticking = None
        self.letters = new_grid()
        for index, tile in enumerate(self.tiles):
            tile.configure(text=self.letters[index].upper())
        self.found = []
        self.score = 0
        self.remaining = ROUND_SECONDS
        self.points.configure(text="0")
        self.clock.configure(text="3:00", fg=mavis_ui.GLOW)
        self.words.delete("1.0", "end")
        self.message.configure(text="New grid. Press start.", fg=mavis_ui.DIM)
        self.entry.focus_set()


if __name__ == "__main__":
    App().mainloop()
