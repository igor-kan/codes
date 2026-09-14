; ModuleID = 'algorithms/02_c/graphs/kahn_topological_sort.c'
source_filename = "algorithms/02_c/graphs/kahn_topological_sort.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [45 x i8] c"[C Kahn] FAILED: processed %d nodes, want 6\0A\00", align 1
@str = private unnamed_addr constant [50 x i8] c"[C Kahn] Topological sort verified (6 nodes, DAG)\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local i32 @kahn(ptr noundef readonly captures(none) %0, i32 noundef %1, ptr noundef captures(none) %2, ptr noundef writeonly captures(none) %3) local_unnamed_addr #0 {
  %5 = alloca [100 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %5) #7
  %6 = icmp sgt i32 %1, 0
  br i1 %6, label %7, label %94

7:                                                ; preds = %4
  %8 = zext nneg i32 %1 to i64
  %9 = and i64 %8, 1
  %10 = icmp eq i32 %1, 1
  br i1 %10, label %15, label %11

11:                                               ; preds = %7
  %12 = and i64 %8, 2147483646
  br label %32

13:                                               ; preds = %55
  %14 = icmp eq i64 %9, 0
  br i1 %14, label %27, label %15

15:                                               ; preds = %13, %7
  %16 = phi i64 [ 0, %7 ], [ %57, %13 ]
  %17 = phi i32 [ 0, %7 ], [ %56, %13 ]
  %18 = icmp ne i64 %9, 0
  tail call void @llvm.assume(i1 %18)
  %19 = getelementptr inbounds nuw i32, ptr %2, i64 %16
  %20 = load i32, ptr %19, align 4, !tbaa !5
  %21 = icmp eq i32 %20, 0
  br i1 %21, label %22, label %27

22:                                               ; preds = %15
  %23 = add nsw i32 %17, 1
  %24 = sext i32 %17 to i64
  %25 = getelementptr inbounds i32, ptr %5, i64 %24
  %26 = trunc nuw nsw i64 %16 to i32
  store i32 %26, ptr %25, align 4, !tbaa !5
  br label %27

27:                                               ; preds = %15, %22, %13
  %28 = phi i32 [ %56, %13 ], [ %23, %22 ], [ %17, %15 ]
  %29 = icmp sgt i32 %28, 0
  br i1 %29, label %30, label %94

30:                                               ; preds = %27
  %31 = zext nneg i32 %1 to i64
  br label %63

32:                                               ; preds = %55, %11
  %33 = phi i64 [ 0, %11 ], [ %57, %55 ]
  %34 = phi i32 [ 0, %11 ], [ %56, %55 ]
  %35 = phi i64 [ 0, %11 ], [ %58, %55 ]
  %36 = getelementptr inbounds nuw i32, ptr %2, i64 %33
  %37 = load i32, ptr %36, align 4, !tbaa !5
  %38 = icmp eq i32 %37, 0
  br i1 %38, label %39, label %44

39:                                               ; preds = %32
  %40 = add nsw i32 %34, 1
  %41 = sext i32 %34 to i64
  %42 = getelementptr inbounds i32, ptr %5, i64 %41
  %43 = trunc nuw nsw i64 %33 to i32
  store i32 %43, ptr %42, align 4, !tbaa !5
  br label %44

44:                                               ; preds = %32, %39
  %45 = phi i32 [ %40, %39 ], [ %34, %32 ]
  %46 = or disjoint i64 %33, 1
  %47 = getelementptr inbounds nuw i32, ptr %2, i64 %46
  %48 = load i32, ptr %47, align 4, !tbaa !5
  %49 = icmp eq i32 %48, 0
  br i1 %49, label %50, label %55

50:                                               ; preds = %44
  %51 = add nsw i32 %45, 1
  %52 = sext i32 %45 to i64
  %53 = getelementptr inbounds i32, ptr %5, i64 %52
  %54 = trunc nuw nsw i64 %46 to i32
  store i32 %54, ptr %53, align 4, !tbaa !5
  br label %55

55:                                               ; preds = %50, %44
  %56 = phi i32 [ %51, %50 ], [ %45, %44 ]
  %57 = add nuw nsw i64 %33, 2
  %58 = add i64 %35, 2
  %59 = icmp eq i64 %58, %12
  br i1 %59, label %13, label %32, !llvm.loop !9

60:                                               ; preds = %88
  %61 = zext nneg i32 %89 to i64
  %62 = icmp samesign ult i64 %66, %61
  br i1 %62, label %63, label %92, !llvm.loop !11

63:                                               ; preds = %30, %60
  %64 = phi i64 [ 0, %30 ], [ %66, %60 ]
  %65 = phi i32 [ %28, %30 ], [ %89, %60 ]
  %66 = add nuw nsw i64 %64, 1
  %67 = getelementptr inbounds nuw i32, ptr %5, i64 %64
  %68 = load i32, ptr %67, align 4, !tbaa !5
  %69 = getelementptr inbounds nuw i32, ptr %3, i64 %64
  store i32 %68, ptr %69, align 4, !tbaa !5
  %70 = sext i32 %68 to i64
  %71 = getelementptr inbounds [100 x i32], ptr %0, i64 %70
  br label %72

72:                                               ; preds = %63, %88
  %73 = phi i64 [ 0, %63 ], [ %90, %88 ]
  %74 = phi i32 [ %65, %63 ], [ %89, %88 ]
  %75 = getelementptr inbounds nuw i32, ptr %71, i64 %73
  %76 = load i32, ptr %75, align 4, !tbaa !5
  %77 = icmp eq i32 %76, 0
  br i1 %77, label %88, label %78

78:                                               ; preds = %72
  %79 = getelementptr inbounds nuw i32, ptr %2, i64 %73
  %80 = load i32, ptr %79, align 4, !tbaa !5
  %81 = add nsw i32 %80, -1
  store i32 %81, ptr %79, align 4, !tbaa !5
  %82 = icmp eq i32 %81, 0
  br i1 %82, label %83, label %88

83:                                               ; preds = %78
  %84 = add nuw nsw i32 %74, 1
  %85 = zext nneg i32 %74 to i64
  %86 = getelementptr inbounds nuw i32, ptr %5, i64 %85
  %87 = trunc nuw nsw i64 %73 to i32
  store i32 %87, ptr %86, align 4, !tbaa !5
  br label %88

88:                                               ; preds = %72, %78, %83
  %89 = phi i32 [ %84, %83 ], [ %74, %78 ], [ %74, %72 ]
  %90 = add nuw nsw i64 %73, 1
  %91 = icmp eq i64 %90, %31
  br i1 %91, label %60, label %72, !llvm.loop !12

92:                                               ; preds = %60
  %93 = trunc nuw nsw i64 %66 to i32
  br label %94

94:                                               ; preds = %4, %92, %27
  %95 = phi i32 [ 0, %27 ], [ %93, %92 ], [ 0, %4 ]
  call void @llvm.lifetime.end.p0(ptr nonnull %5) #7
  ret i32 %95
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  %1 = alloca [100 x i32], align 16
  %2 = alloca [100 x [100 x i32]], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %2) #7
  call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(40000) %2, i8 0, i64 40000, i1 false)
  %3 = getelementptr inbounds nuw i8, ptr %2, i64 2000
  %4 = getelementptr inbounds nuw i8, ptr %2, i64 2008
  store i32 1, ptr %4, align 8, !tbaa !5
  store i32 1, ptr %3, align 16, !tbaa !5
  %5 = getelementptr inbounds nuw i8, ptr %2, i64 1600
  store i32 1, ptr %5, align 16, !tbaa !5
  %6 = getelementptr inbounds nuw i8, ptr %2, i64 1604
  store i32 1, ptr %6, align 4, !tbaa !5
  %7 = getelementptr inbounds nuw i8, ptr %2, i64 812
  store i32 1, ptr %7, align 4, !tbaa !5
  %8 = getelementptr inbounds nuw i8, ptr %2, i64 1204
  store i32 1, ptr %8, align 4, !tbaa !5
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #7
  store i32 4, ptr %1, align 16, !tbaa !5
  %9 = getelementptr inbounds nuw i8, ptr %1, i64 4
  store i32 5, ptr %9, align 4, !tbaa !5
  br label %10

10:                                               ; preds = %0, %97
  %11 = phi i32 [ 2, %0 ], [ %33, %97 ]
  %12 = phi i32 [ 2, %0 ], [ %46, %97 ]
  %13 = phi i32 [ 1, %0 ], [ %59, %97 ]
  %14 = phi i32 [ 1, %0 ], [ %72, %97 ]
  %15 = phi i32 [ 0, %0 ], [ %85, %97 ]
  %16 = phi i32 [ 0, %0 ], [ %98, %97 ]
  %17 = phi i64 [ 0, %0 ], [ %100, %97 ]
  %18 = phi i32 [ 2, %0 ], [ %99, %97 ]
  %19 = getelementptr inbounds nuw i32, ptr %1, i64 %17
  %20 = load i32, ptr %19, align 4, !tbaa !5
  %21 = sext i32 %20 to i64
  %22 = getelementptr inbounds [100 x i32], ptr %2, i64 %21
  %23 = load i32, ptr %22, align 16, !tbaa !5
  %24 = icmp eq i32 %23, 0
  br i1 %24, label %32, label %25

25:                                               ; preds = %10
  %26 = add nsw i32 %11, -1
  %27 = icmp eq i32 %26, 0
  br i1 %27, label %28, label %32

28:                                               ; preds = %25
  %29 = add nuw nsw i32 %18, 1
  %30 = zext nneg i32 %18 to i64
  %31 = getelementptr inbounds nuw i32, ptr %1, i64 %30
  store i32 0, ptr %31, align 4, !tbaa !5
  br label %32

32:                                               ; preds = %28, %25, %10
  %33 = phi i32 [ %11, %10 ], [ 0, %28 ], [ %26, %25 ]
  %34 = phi i32 [ %18, %10 ], [ %29, %28 ], [ %18, %25 ]
  %35 = getelementptr inbounds nuw i8, ptr %22, i64 4
  %36 = load i32, ptr %35, align 4, !tbaa !5
  %37 = icmp eq i32 %36, 0
  br i1 %37, label %45, label %38

38:                                               ; preds = %32
  %39 = add nsw i32 %12, -1
  %40 = icmp eq i32 %39, 0
  br i1 %40, label %41, label %45

41:                                               ; preds = %38
  %42 = add nuw nsw i32 %34, 1
  %43 = zext nneg i32 %34 to i64
  %44 = getelementptr inbounds nuw i32, ptr %1, i64 %43
  store i32 1, ptr %44, align 4, !tbaa !5
  br label %45

45:                                               ; preds = %41, %38, %32
  %46 = phi i32 [ %12, %32 ], [ 0, %41 ], [ %39, %38 ]
  %47 = phi i32 [ %34, %32 ], [ %42, %41 ], [ %34, %38 ]
  %48 = getelementptr inbounds nuw i8, ptr %22, i64 8
  %49 = load i32, ptr %48, align 8, !tbaa !5
  %50 = icmp eq i32 %49, 0
  br i1 %50, label %58, label %51

51:                                               ; preds = %45
  %52 = add nsw i32 %13, -1
  %53 = icmp eq i32 %52, 0
  br i1 %53, label %54, label %58

54:                                               ; preds = %51
  %55 = add nuw nsw i32 %47, 1
  %56 = zext nneg i32 %47 to i64
  %57 = getelementptr inbounds nuw i32, ptr %1, i64 %56
  store i32 2, ptr %57, align 4, !tbaa !5
  br label %58

58:                                               ; preds = %54, %51, %45
  %59 = phi i32 [ %13, %45 ], [ 0, %54 ], [ %52, %51 ]
  %60 = phi i32 [ %47, %45 ], [ %55, %54 ], [ %47, %51 ]
  %61 = getelementptr inbounds nuw i8, ptr %22, i64 12
  %62 = load i32, ptr %61, align 4, !tbaa !5
  %63 = icmp eq i32 %62, 0
  br i1 %63, label %71, label %64

64:                                               ; preds = %58
  %65 = add nsw i32 %14, -1
  %66 = icmp eq i32 %65, 0
  br i1 %66, label %67, label %71

67:                                               ; preds = %64
  %68 = add nuw nsw i32 %60, 1
  %69 = zext nneg i32 %60 to i64
  %70 = getelementptr inbounds nuw i32, ptr %1, i64 %69
  store i32 3, ptr %70, align 4, !tbaa !5
  br label %71

71:                                               ; preds = %67, %64, %58
  %72 = phi i32 [ %14, %58 ], [ 0, %67 ], [ %65, %64 ]
  %73 = phi i32 [ %60, %58 ], [ %68, %67 ], [ %60, %64 ]
  %74 = getelementptr inbounds nuw i8, ptr %22, i64 16
  %75 = load i32, ptr %74, align 16, !tbaa !5
  %76 = icmp eq i32 %75, 0
  br i1 %76, label %84, label %77

77:                                               ; preds = %71
  %78 = add nsw i32 %15, -1
  %79 = icmp eq i32 %78, 0
  br i1 %79, label %80, label %84

80:                                               ; preds = %77
  %81 = add nuw nsw i32 %73, 1
  %82 = zext nneg i32 %73 to i64
  %83 = getelementptr inbounds nuw i32, ptr %1, i64 %82
  store i32 4, ptr %83, align 4, !tbaa !5
  br label %84

84:                                               ; preds = %80, %77, %71
  %85 = phi i32 [ %15, %71 ], [ 0, %80 ], [ %78, %77 ]
  %86 = phi i32 [ %73, %71 ], [ %81, %80 ], [ %73, %77 ]
  %87 = getelementptr inbounds nuw i8, ptr %22, i64 20
  %88 = load i32, ptr %87, align 4, !tbaa !5
  %89 = icmp eq i32 %88, 0
  br i1 %89, label %97, label %90

90:                                               ; preds = %84
  %91 = add nsw i32 %16, -1
  %92 = icmp eq i32 %91, 0
  br i1 %92, label %93, label %97

93:                                               ; preds = %90
  %94 = add nuw nsw i32 %86, 1
  %95 = zext nneg i32 %86 to i64
  %96 = getelementptr inbounds nuw i32, ptr %1, i64 %95
  store i32 5, ptr %96, align 4, !tbaa !5
  br label %97

97:                                               ; preds = %93, %90, %84
  %98 = phi i32 [ %16, %84 ], [ 0, %93 ], [ %91, %90 ]
  %99 = phi i32 [ %86, %84 ], [ %94, %93 ], [ %86, %90 ]
  %100 = add nuw nsw i64 %17, 1
  %101 = zext nneg i32 %99 to i64
  %102 = icmp samesign ult i64 %100, %101
  br i1 %102, label %10, label %103, !llvm.loop !11

103:                                              ; preds = %97
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #7
  %104 = icmp eq i64 %100, 6
  br i1 %104, label %108, label %105

105:                                              ; preds = %103
  %106 = trunc nuw nsw i64 %100 to i32
  %107 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %106)
  br label %110

108:                                              ; preds = %103
  %109 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str)
  br label %110

110:                                              ; preds = %108, %105
  %111 = phi i32 [ 1, %105 ], [ 0, %108 ]
  call void @llvm.lifetime.end.p0(ptr nonnull %2) #7
  ret i32 %111
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: write)
declare void @llvm.memset.p0.i64(ptr writeonly captures(none), i8, i64, i1 immarg) #3

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #4

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #5

; Function Attrs: nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write)
declare void @llvm.assume(i1 noundef) #6

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: write) }
attributes #4 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #5 = { nofree nounwind }
attributes #6 = { nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write) }
attributes #7 = { nounwind }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
!11 = distinct !{!11, !10}
!12 = distinct !{!12, !10}
