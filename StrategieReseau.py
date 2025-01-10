from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain):
        return -1, {}, []

    def valider(self, noeuds, arcs, t: Terrain) -> bool:
        return True

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain):
        noeud_entree = -1
        noeuds = {}
        arcs = []

        for i, ligne in enumerate(t.cases):
            for j, c in enumerate(ligne):
                if c == Case.ENTREE:
                    noeud_entree = len(noeuds)
                    noeuds[noeud_entree] = (i, j)
                elif c == Case.CLIENT:
                    noeuds[len(noeuds)] = (i, j)

        for n1 in noeuds:
            for n2 in noeuds:
                if n1 != n2:
                    if abs(noeuds[n1][0] - noeuds[n2][0]) + abs(noeuds[n1][1] - noeuds[n2][1]) == 1:
                        arcs.append((n1, n2))

        return noeud_entree, noeuds, arcs

